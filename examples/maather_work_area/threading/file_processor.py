import os
import threading
import time
import hashlib



class FileProcessor:
    def __init__(self, directory):
        self.directory = directory
        self.processed_files = set()
        self.processed_hashes = set()
        self.monitor_thread = threading.Thread(target=self.monitor_directory)  # Corrected target
        self.monitor_thread.daemon = True  # Daemonize the monitor thread to exit when the main thread exits
        self.monitor_thread.start()
    
    def monitor_directory(self):
        print("directory monitoring started")
        while True:
            for filename in os.listdir(self.directory):
                file_hash = self._calculate_file_hash(self.directory + "/" + filename)
                if file_hash not in self.processed_hashes:
                    print("found a new file!\n "+ filename)
                    self.processed_files.add(filename)
                    self.processed_hashes.add(file_hash)
                    process_thread = threading.Thread(target=self._process_file, args=(filename,))
                    process_thread.start()
            time.sleep(1)

    def _process_file(self, filename):
        file_path = os.path.join(self.directory, filename)
        file_hash = self._calculate_file_hash(file_path)
        processed_content = "processed content of " + filename
        self._save_result(filename, file_hash, processed_content)
    
    def _calculate_file_hash(self, file_path):
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()
    
    def _save_result(self, filename, file_hash, processed_content):
        result_filename = "result.txt"
        with open(result_filename, "a") as result_file:
            result_file.write(f"{filename},{file_hash},{processed_content}\n")
    

if __name__ == "__main__":
    monitored_directory = "monitored"
    file_processor = FileProcessor(monitored_directory)
    
    while True:
        time.sleep(1)
