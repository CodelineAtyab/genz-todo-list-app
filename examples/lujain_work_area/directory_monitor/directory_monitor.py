import sys
import time
import logging
import threading
from queue import Queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Function to process the file
def process_file(file_path):
    # Placeholder for file processing logic
    processed_content = f"Processed content of {file_path}"
    return processed_content

# Watchdog event handler for file system events
class FileEventHandler(FileSystemEventHandler):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def on_created(self, event):
        if not event.is_directory:
            self.queue.put(event.src_path)

# Main thread to save processed results to a file
def save_results(queue):
    result_filename = "processing_log.txt"  # Name of the result file
    while True:
        file_path = queue.get()
        processed_content = process_file(file_path)
        with open(result_filename, 'a') as result_file:
            result_file.write(f"{file_path}: {processed_content}\n")
        logging.info(f"Processed file '{file_path}' and saved result to '{result_filename}'")
        queue.task_done()

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Set up the queue for inter-thread communication
    queue = Queue()

    # Start the main thread to save processed results
    result_thread = threading.Thread(target=save_results, args=(queue,))
    result_thread.daemon = True
    result_thread.start()

    # Set up the file system monitor using Watchdog
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = FileEventHandler(queue)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        # Keep the main thread running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the file system observer if KeyboardInterrupt (Ctrl+C) is detected
        observer.stop()

    # Wait for the observer thread to terminate
    observer.join()

# Watchdog is used to monitor file system events (such as file creation) in real-time.
# It triggers events when changes occur in the monitored directory.
# These events are handled by the FileEventHandler class, which puts the file paths into a queue for processing.
# Meanwhile, a separate thread continuously retrieves file paths from the queue, processes them, and saves the results to a file.
