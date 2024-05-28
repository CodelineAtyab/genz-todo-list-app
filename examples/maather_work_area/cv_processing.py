import glob
import os
import time
import traceback
import json
from queue import Empty
from multiprocessing import Process, Queue
from pyresparser import ResumeParser

def process_cv(process_id: str, cv_queue: Queue, res_queue: Queue):
    print(f"Process {process_id}: Running.")
    try:
        while True:
            try:
                cv_file_path = cv_queue.get(timeout=3)
                data = ResumeParser(cv_file_path).get_extracted_data()
                print(f"Process {process_id}: Data: {data}")
                res_queue.put((cv_file_path, data))
            except Empty:
                print(f"Process {process_id}: Queue is empty.")
                break
            except Exception:
                print(f"Process {process_id}: Exception {traceback.format_exc()}")
    except Exception:
        print(f"Process {process_id}: Exception {traceback.format_exc()}")

def write_result_to_file(process_id, res_queue: Queue):
    print(f"Process {process_id}: Running.")
    result_dir = "./results"
    os.makedirs(result_dir, exist_ok=True)
    while True:
        try:
            cv_file_path, res_data = res_queue.get(timeout=3)
            base_name = os.path.basename(cv_file_path)
            name, ext = os.path.splitext(base_name)
            unique_file_path = os.path.join(result_dir, f"{name}_{int(time.time())}.json")
            with open(unique_file_path, "w") as res_file:
                json.dump(res_data, res_file, indent=4)
            print(f"Process {process_id}: Saved result to {unique_file_path}")
        except Empty:
            print(f"Process {process_id}: Result Queue is empty.")
            time.sleep(3)  # Sleep briefly to avoid busy-waiting
        except Exception:
            print(traceback.format_exc())

def monitor_directory(cv_queue: Queue, directory: str):
    print("Producer: Monitoring directory for new CV files.")
    processed_files = set()
    while True:
        try:
            list_of_uploaded_cvs = glob.glob(f"{directory}/*.pdf")
            for curr_cv_file_path in list_of_uploaded_cvs:
                if curr_cv_file_path not in processed_files:
                    cv_queue.put(curr_cv_file_path)
                    processed_files.add(curr_cv_file_path)
                    print(f"Producer: Added {curr_cv_file_path} to queue.")
            time.sleep(5)  # Check for new files every 5 seconds
        except Exception:
            print(f"Producer: Exception {traceback.format_exc()}")

if __name__ == "__main__":
    main_cv_file_queue = Queue(maxsize=0)
    result_skills_queue = Queue(maxsize=0)
    no_of_consumer_processes = 7  # Utilize all CPU cores

    # Start the producer process
    producer_process = Process(target=monitor_directory, args=(main_cv_file_queue, "./resumes"))
    producer_process.start()

    # Start the result consumer process
    res_consumer_process = Process(target=write_result_to_file, args=("res_con", result_skills_queue))
    res_consumer_process.start()

    # Start the consumer processes
    list_of_consumer_processes = []
    for pid in range(1, no_of_consumer_processes + 1):
        curr_process = Process(target=process_cv, args=(str(pid), main_cv_file_queue, result_skills_queue))
        list_of_consumer_processes.append(curr_process)
        curr_process.start()

    # Wait for all consumer processes to complete
    for curr_consumer_process in list_of_consumer_processes:
        curr_consumer_process.join()

    # Ensure the result consumer process completes
    res_consumer_process.join()

    # Keep the producer process running indefinitely
    producer_process.join()

    print("Exiting ...")
