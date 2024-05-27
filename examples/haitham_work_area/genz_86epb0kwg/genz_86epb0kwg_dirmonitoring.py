import os
import time
import threading
from queue import Queue

MONITOR_DIR = "C:/Users/71521/Desktop/newrepo/genz-todo-list-app/examples/haitham_work_area/genz_86epb0kwg/dirtest"

RESULT_FILE = "results.txt"

file_queue = Queue()


def file_monitor():
    processed_files = set()
    while True:
        try:
            current_files = set(os.listdir(MONITOR_DIR))
            new_files = current_files - processed_files
            for filename in new_files:
                full_path = os.path.join(MONITOR_DIR, filename)
                if os.path.isfile(full_path):
                    file_queue.put(full_path)
                    processed_files.add(filename)
                    print(f"Detected new file: {filename}")
            time.sleep(2)
        except KeyboardInterrupt:
            return


def process_files():
    while True:
        filename = file_queue.get()
        if filename == "STOP":
            return
        try:
            with open(filename, 'r') as file:
                content = file.read()
            count_a = content.lower().count('a')
            result = f"{os.path.basename(filename)}, a={count_a}\n"
            result_queue.put(result)
            print(f"Processed {filename}: 'a' appears {count_a} times")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
        finally:
            file_queue.task_done()


result_queue = Queue()


def save_results():
    while True:
        result = result_queue.get()
        if result == "STOP":
            return
        with open(RESULT_FILE, 'a') as result_file:
            result_file.write(result)
            print(f"Result saved for {result.split(',')[0]}")
        result_queue.task_done()


monitor_thread = threading.Thread(target=file_monitor)
monitor_thread.daemon = True
monitor_thread.start()

processing_thread = threading.Thread(target=process_files)
processing_thread.daemon = True
processing_thread.start()

save_results_thread = threading.Thread(target=save_results)
save_results_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
    file_queue.put("STOP")
    result_queue.put("STOP")
    processing_thread.join()
    save_results_thread.join()
    print("Stopped.")
