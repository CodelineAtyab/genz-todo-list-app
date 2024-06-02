import os
import time
import hashlib
from multiprocessing import Process, Queue
from pyresparser import ResumeParser
import json
from queue import Empty


def monitor_directory(directory, process_queue, processed_files):
    while True:
        for filename in os.listdir(directory):
            if filename.endswith('.pdf') or filename.endswith('.docx'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'rb') as file:
                    file_hash = hashlib.sha256(file.read()).hexdigest()
                if filename not in processed_files or processed_files[filename] != file_hash:
                    process_queue.put((filename, file_hash, filepath))
        time.sleep(3)


def process_cv_files(process_queue, result_queue):
    while True:
        try:
            filename, file_hash, filepath = process_queue.get(timeout=1)
            data = ResumeParser(filepath).get_extracted_data()
            result_queue.put((filename, data))
            new_file_path = os.path.join(os.path.dirname(filename), "processed_" + os.path.basename(filename))
            os.rename(filename, new_file_path)
            print(f"Renamed file to: {new_file_path}")
        except Empty:
            pass


def write_results(result_queue, result_directory):
    while True:
        try:
            filename, data = result_queue.get(timeout=1)
            result_filename = os.path.join(result_directory, filename + '.json')
            with open(result_filename, 'w') as f:
                json.dump(data, f)
        except Empty:
            pass


if __name__ == '__main__':

    # Define directories and number of consumer processes
    cv_directory = './cvs'
    result_directory = './results'
    num_consumers = 3

    # Create Queues for communication between processes
    process_queue = Queue()
    result_queue = Queue()

    # Dictionary to keep track of processed files and their hashes
    processed_files = dict()

    # Start producer process
    producer_process = Process(target=monitor_directory, args=(cv_directory, process_queue, processed_files))
    producer_process.start()

    # Start consumer processes
    consumer_processes = []
    for _ in range(num_consumers):
        consumer_process = Process(target=process_cv_files, args=(process_queue, result_queue))
        consumer_process.start()
        consumer_processes.append(consumer_process)

    # Start result monitor process
    result_monitor_process = Process(target=write_results, args=(result_queue, result_directory))
    result_monitor_process.start()

    # Join all processes to ensure proper termination
    producer_process.join()
    for consumer_process in consumer_processes:
        consumer_process.join()
    result_monitor_process.join()


