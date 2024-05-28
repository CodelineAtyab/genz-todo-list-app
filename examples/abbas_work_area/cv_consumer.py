import traceback
from queue import Empty
from pyresparser import ResumeParser
from multiprocessing import Process, Queue
import hashlib
import json


class CVConsumer:
    def __init__(self):
        self.hashes = set()
        self.result_file_name = "./Documents/result.txt"
        self.load_hashes()

    def load_hashes(self):
        """
        Load existing hashes from the result.txt.
        """
        try:
            lines = self.open_read_file('r')
            for line in lines:
                if 'SHA256 Hash:' in line:
                    hash_value = line.split('SHA256 Hash: ')[1].strip().split(',')[0]
                    self.hashes.add(hash_value)
        except FileNotFoundError:
            print("file not found")
        except Exception as e:
            print(f"Error loading hashes: {e}")

    def write_result_to_file(self, process_id, res_queue: Queue):
        """
        Consume the result Queue and save the skills to a file.
        :param res_queue: The Queue containing results.
        :param process_id: Identifier for this process.
        :return:
        """
        print(f"Process {process_id}: Running.")
        
        while True:
            try:
                res_data = res_queue.get(timeout=3)
                # Retrieve the precomputed hash from the result data
                sha256_hash = res_data.get('hash')
                if sha256_hash in self.hashes:
                    print(f"Process {process_id}: Duplicate result found. Skipping.")
                    continue
                
                res_data_str = json.dumps(res_data)
                filename = res_data.get('filename', 'unknown')
                # Write result and hash to file
                result = f"Result: {res_data_str}, SHA256 Hash: {sha256_hash}, Filename: {filename}\n"
                self.open_read_file("a", result)

            except Empty:
                print(f"Process {process_id}: Result Queue is empty.")
            except Exception as e:
                print(traceback.format_exc(), e)

    def process_cv(self, process_id: str, cv_queue: Queue, res_queue: Queue):
        print(f"Process {process_id}: Running.")

        try:
            while True:
                cv_file_path = cv_queue.get(timeout=3)
                # Compute SHA256 hash for the CV file content
                cv_file_data = self.open_read_file(state='rb', file_path=cv_file_path)
                sha256_hash = hashlib.sha256(cv_file_data).hexdigest()
                
                # Check if the hash already exists
                if sha256_hash in self.hashes:
                    print(f"Process {process_id}: Duplicate CV found. Skipping.")
                    continue
                
                data = ResumeParser(cv_file_path).get_extracted_data()
                data['filename'] = cv_file_path
                data['hash'] = sha256_hash
                print(f"Process {process_id}: Data: {data}")
                res_queue.put(data)
                
                # Add the new hash to the set
                self.hashes.add(sha256_hash)
        except Empty:
            print(f"Process {process_id}: Queue is empty.")
        except Exception:
            print(f"Process {process_id}: Exception {traceback.format_exc()}")

    @staticmethod
    def open_read_file(self, state, result="", file_path="./Documents/result.txt"):
        with open(file_path, state) as res_file:
            if state == 'a':
                res_file.write(result)
            elif state == 'r':
                return res_file.readlines()
            elif state == 'rb':
                return res_file.read()
        return None
