import os
import glob
import traceback
import time
import json
import hashlib

from queue import Empty
from multiprocessing import Process, Queue, cpu_count
from pyresparser import ResumeParser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class CVHandler(FileSystemEventHandler):
    def __init__(self, queue):
        self.queue = queue

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"Detected new file: {event.src_path}")
        self.queue.put(event.src_path)


def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def process_cv(process_id: str, cv_queue: Queue, res_queue: Queue):
    print(f"Process {process_id}: Running.")
    while True:
        try:
            cv_file_path = cv_queue.get(timeout=3)
            print(f"Process {process_id}: Processing {cv_file_path}")
            data = ResumeParser(cv_file_path).get_extracted_data()
            res_queue.put((cv_file_path, data))
        except Empty:
            continue
        except Exception:
            print(f"Process {process_id}: Exception {traceback.format_exc()}")


def write_result_to_file(process_id, res_queue: Queue):
    print(f"Process {process_id}: Running.")
    while True:
        try:
            cv_file_path, res_data = res_queue.get(timeout=3)
            unique_filename = f"./results/{os.path.basename(cv_file_path)}_{hash_file(cv_file_path)}.json"
            with open(unique_filename, "w") as res_file:
                json.dump(res_data, res_file)
            print(f"Process {process_id}: Wrote results to {unique_filename}")
        except Empty:
            continue
        except Exception:
            print(traceback.format_exc())


if __name__ == "__main__":
    cv_dir = "./cvs/"
    os.makedirs(cv_dir, exist_ok=True)
    os.makedirs("./results", exist_ok=True)

    main_cv_file_queue = Queue(maxsize=0)
    result_skills_queue = Queue(maxsize=0)

    # Use watchdog to monitor the directory for new CV files
    event_handler = CVHandler(main_cv_file_queue)
    observer = Observer()
    observer.schedule(event_handler, path=cv_dir, recursive=False)
    observer.start()

    # Start result consumer process
    res_consumer_process = Process(target=write_result_to_file, args=("res_con", result_skills_queue))
    res_consumer_process.start()

    # Start CV consumer processes
    no_of_consumer_processes = min(6, cpu_count() - 2)  # Ensuring we have at least 1 core for producer and 1 for result writer
    list_of_consumer_processes = []
    for pid in range(1, no_of_consumer_processes + 1):
        curr_process = Process(target=process_cv, args=(str(pid), main_cv_file_queue, result_skills_queue))
        list_of_consumer_processes.append(curr_process)
        curr_process.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Ending the process")

    observer.stop()
    observer.join()

    for curr_consumer_process in list_of_consumer_processes:
        curr_consumer_process.terminate()
        curr_consumer_process.join()

    res_consumer_process.terminate()
    res_consumer_process.join()

    print("Done")
