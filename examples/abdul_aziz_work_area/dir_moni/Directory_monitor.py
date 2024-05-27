import os
import time
import threading
import hashlib
from queue import Queue

# Directory to monitor
WATCHED_DIR = "watched_directory"
# Output file to save results
OUTPUT_FILE = "processed_results.txt"

# Queue to hold filenames to be processed
file_queue = Queue()
# Dictionary to store file hashes
file_hashes = {}


def compute_hash(file_path):
    """Compute the SHA-256 hash of a file's content."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def monitor_directory():
    """Monitor the directory for newly uploaded or modified files."""
    while True:
        # Get the list of files in the directory
        current_files = os.listdir(WATCHED_DIR)
        for file in current_files:
            file_path = os.path.join(WATCHED_DIR, file)
            if os.path.isfile(file_path):
                file_hash = compute_hash(file_path)
                if file not in file_hashes or file_hashes[file] != file_hash:
                    file_queue.put((file, file_hash))
        time.sleep(1)  # Polling interval (1 second)


def process_files():
    """Process files from the queue."""
    while True:
        # Get a file from the queue
        item = file_queue.get()
        if item is None:
            break  # Stop processing if sentinel value is detected

        file, current_hash = item
        # Check if the file has been modified
        if file in file_hashes and file_hashes[file] == current_hash:
            modified = False
        else:
            modified = True
            file_hashes[file] = current_hash

        # Save result to output file
        with open(OUTPUT_FILE, 'a') as out_f:
            out_f.write(f"{file},{current_hash},{modified}\n")

        file_queue.task_done()


def main():
    # Create the watched directory if it doesn't exist
    os.makedirs(WATCHED_DIR, exist_ok=True)

    # Start the monitor thread
    monitor_thread = threading.Thread(target=monitor_directory, daemon=True)
    monitor_thread.start()

    # Start the processing thread
    processing_thread = threading.Thread(target=process_files, daemon=True)
    processing_thread.start()

    # Wait for all threads to finish (in this case, they run indefinitely)
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Shutting down...")

        # Send sentinel value to stop the processing thread
        file_queue.put(None)
        processing_thread.join()


if __name__ == "__main__":
    main()
