import time
import threading
import queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Global variables
directory = "./"
processed_files = set()


# Event handler for file events
class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file = event.src_path
            if file not in processed_files:
                print(f"New file created: {file}")
                process_queue.put(file)
                processed_files.add(file)


# Monitor thread function
def monitor_files():
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, directory)
    observer.start()
    try:
        while True:
            time.sleep(2)  # to stop when a signal is received
    except KeyboardInterrupt:
        observer.stop()
    # observer.join()


# Process thread function
def process_files(content=None):
    while True:
        if not process_queue.empty():
            file = process_queue.get()
            # Process the file
            result = process_file_content(file)  # Process file content
            save_queue.put((file, result))


# Function to process file content
def process_file_content(file):
    # Print file path for debugging
    print(f"Processing file: {file}")

    # Read content from file and print it
    with open(file, "r") as f:
        f.flush()  # Flush file buffer
        content = f.read()
        if content:
            print(f"File: {file}\nContent:\n{content}\n")
        else:
            print(f"File {file} is empty")
    return file, content


# Main thread function to save results
def save_results():
    while True:
        if not save_queue.empty():
            file, result = save_queue.get()
            with open("processed_results.txt", "a") as f:
                f.write(f"File Name and Content: {result}\n")
        time.sleep(1)


if __name__ == "__main__":
    process_queue = queue.Queue()
    save_queue = queue.Queue()

    # Create and start threads
    monitor_thread = threading.Thread(target=monitor_files, daemon=True)
    process_thread = threading.Thread(target=process_files, daemon=True)
    save_thread = threading.Thread(target=save_results, daemon=True)

    monitor_thread.start()
    process_thread.start()
    save_thread.start()

    # Join threads
    monitor_thread.join()  # not supposed to exit because of the while loop above
    # process_thread.join()
    # save_thread.join()

