import os
import time
import threading
from queue import Queue
import hashlib


def get_files_from_directory(directory):
    """
    Retrieves a list of file paths from a specified directory.

    :param directory: The path of the directory.
    :return: A list of file paths in the directory.
    """
    if os.path.isdir(directory):
        return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    else:
        return []


def get_file_hash(file_path):
    """
        Calculates the SHA-256 hash of a file's content.

        :param file_path: The path of the file.
        :return: The SHA-256 hash of the file's content.
        """
    block_size = 65536
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buffer = file.read(block_size)
        while len(buffer) > 0:
            sha256_hash.update(buffer)
            buffer = file.read(block_size)
    return sha256_hash.hexdigest()


def monitor_files(queue, source):
    """
    Monitors a directory or a file for new files and adds them to the queue.

    :param queue: The queue to which file paths are added.
    :param source: The directory path or file containing a list of file paths to monitor.
    """
    while True:
        time.sleep(1)  # Adjust as needed
        if os.path.isdir(source):
            files = get_files_from_directory(source)

        for file in files:
            if not (file.startswith("processed_") or os.path.basename(file).startswith("processed_")):
                queue.put(file)


def process_files(queue_in, queue_out, processed_hashes):
    """
    Processes files from the input queue, comparing their hashes to processed ones, and adds to the output queue if not processed.

    :param queue_in: The input queue containing file paths.
    :param queue_out: The output queue to which processed files are added.
    :param processed_hashes: A set containing hashes of processed file content.
    """
    while True:
        file_path = queue_in.get()
        file_hash = get_file_hash(file_path)
        if file_hash not in processed_hashes:
            processed_hashes.add(file_hash)
            with open(file_path, 'r') as f:
                processed_content = f.read()
            queue_out.put((file_path, processed_content))
        else:
            os.remove(file_path)
            print(f'{file_path} content already processed')
        queue_in.task_done()


def save_result(queue):
    """
   Saves the processed result to a file.

   :param queue: The queue containing processed file paths and content.
   """
    while True:
        file_path, processed_content = queue.get()
        new_file_path = os.path.join(os.path.dirname(file_path), "processed_" + os.path.basename(file_path))
        os.remove(file_path)
        with open(new_file_path, 'w') as f:
            f.write(processed_content)
            print(f'content in {file_path}: {processed_content}')
        queue.task_done()


if __name__ == "__main__":
    # Source can be either a directory path or a file containing a list of file paths
    source = "./monitor"

    # Create queues to communicate between threads
    file_queue = Queue()
    processed_queue = Queue()

    # Create a set to store processed file hashes
    processed_hashes = set()

    # Create and start the file monitor thread
    monitor_thread = threading.Thread(target=monitor_files, args=(file_queue, source), daemon=True)
    monitor_thread.start()

    # Create and start the file processor thread
    processor_thread = threading.Thread(target=process_files, args=(file_queue, processed_queue, processed_hashes), daemon=True)
    processor_thread.start()

    # Create and start the result saver thread
    saver_thread = threading.Thread(target=save_result, args=(processed_queue,), daemon=True)
    saver_thread.start()

    try:
        # Keep the main thread running
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")

