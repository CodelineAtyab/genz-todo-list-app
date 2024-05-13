import os
import time
import threading
import hashlib
from pdfminer.high_level import extract_text


class FileProcessor:
    def __init__(self, directory):
        self.directory = directory
        self.result_file = "results.txt"
        self.processed_hashes = self.load_processed_hashes()
        self.file_queue = []
        self.lock = threading.Lock()
        self.monitor_thread = threading.Thread(target=self.monitor_directory, daemon=True)
        self.processing_thread = threading.Thread(target=self.process_files, daemon=True)

    def load_processed_hashes(self):
        processed_hashes = set()
        if os.path.exists(self.result_file):
            with open(self.result_file, 'r') as f:
                for line in f:
                    if line.startswith("Hash: "):
                        processed_hashes.add(line.split()[1])
        return processed_hashes

    def start(self):
        self.monitor_thread.start()
        self.processing_thread.start()

    def monitor_directory(self):
        while True:
            for filename in os.listdir(self.directory):
                file_path = os.path.join(self.directory, filename)
                if os.path.isfile(file_path) and file_path.endswith('.pdf'):
                    with self.lock:
                        self.file_queue.append(file_path)
            time.sleep(1)  # Check directory every 1 second

    def process_files(self):
        while True:
            if self.file_queue:
                file_path = self.file_queue.pop(0)
                file_hash = self.calculate_file_hash(file_path)
                with self.lock:
                    if file_hash in self.processed_hashes:
                        continue
                    else:
                        self.processed_hashes.add(file_hash)
                print(f"Processing file: {file_path}")
                try:
                    content = extract_text(file_path)
                except Exception as e:
                    print(f"Failed to read PDF file: {file_path}. Error: {e}")
                    continue
                num_a = content.count('a')
                result = f"File: {os.path.basename(file_path)}\nHash: {file_hash}\nNumber of 'a': {num_a}\n\n"
                self.save_result(result)
                print(f"Finished processing file: {file_path}")
            else:
                time.sleep(1)  # Sleep when there are no files in the queue

    def save_result(self, result):
        with open(self.result_file, 'a') as result_file:
            result_file.write(result)

    def calculate_file_hash(self, file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()
            file_hash = hashlib.sha256(file_content).hexdigest()
        return file_hash


if __name__ == "__main__":
    directory = "."
    file_processor = FileProcessor(directory)
    file_processor.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
