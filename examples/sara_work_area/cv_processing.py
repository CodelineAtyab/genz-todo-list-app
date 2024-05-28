import glob
import traceback
import time
from queue import Empty
from multiprocessing import Process, Queue
from pyresparser import ResumeParser
import os

class DirectoryMonitor:
    def __init__(self, cv_queue: Queue, cv_directory: str):
        self.cv_queue = cv_queue
        self.cv_directory = cv_directory
        self.processed_files = set()

    def run(self):
        while True:
            for file_name in os.listdir(self.cv_directory):
                if file_name.endswith(".pdf") and file_name not in self.processed_files:
                    file_path = os.path.join(self.cv_directory, file_name)
                    print(f"New CV detected: {file_path}")
                    self.cv_queue.put(file_path)
                    self.processed_files.add(file_name)
            time.sleep(1)

class Consumer:
    def __init__(self, process_id: str, cv_queue: Queue, result_file_name: str):
        self.process_id = process_id
        self.cv_queue = cv_queue
        self.result_file_name = result_file_name

    def process_cv(self):
        print(f"Process {self.process_id}: Running.")
        while True:
            try:
                cv_file_path = self.cv_queue.get(timeout=15)
                if cv_file_path is None:
                    print(f"Process {self.process_id}: Received termination signal.")
                    break
                print(f"Process {self.process_id}: Processing {cv_file_path}")
                data = ResumeParser(cv_file_path).get_extracted_data()
                with open(self.result_file_name, "a") as res_file:
                    res_file.write(str(data) + '\n')
                print(f"Process {self.process_id}: Wrote data to file.")
            except Empty:
                print(f"Process {self.process_id}: Queue is empty.")
                break
            except Exception:
                print(f"Process {self.process_id}: Exception {traceback.format_exc()}")

if __name__ == "__main__":
    cv_directory = "./uploads"
    result_file_name = "./result.txt"

    cv_queue = Queue()
    directory_monitor = DirectoryMonitor(cv_queue, cv_directory)
    monitor_process = Process(target=directory_monitor.run)
    monitor_process.start()

    consumer_processes = []
    for pid in range(1, 8):
        consumer = Consumer(str(pid), cv_queue, result_file_name)
        consumer_process = Process(target=consumer.process_cv)
        consumer_processes.append(consumer_process)
        consumer_process.start()

    try:
        for consumer_process in consumer_processes:
            consumer_process.join()
    except KeyboardInterrupt:
        for consumer_process in consumer_processes:
            consumer_process.terminate()
        monitor_process.terminate()

