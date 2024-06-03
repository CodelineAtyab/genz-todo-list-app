import traceback
from queue import Empty
from multiprocessing import Queue

from pyresparser import ResumeParser


class ResumeParserProcess:
    def __init__(self, cv_queue: Queue, result_queue: Queue):
        self.cv_queue = cv_queue
        self.result_queue = result_queue

    def run(self, process_id: str):
        print(f"Process {process_id}: Running.")

        try:
            while not self.cv_queue.empty():
                cv_file_path = self.cv_queue.get(timeout=3)
                data = ResumeParser(cv_file_path).get_extracted_data()
                print(f"Process {process_id}: Data: {data}")
                self.result_queue.put(data)
        except Empty:
            print(f"Process {process_id}: Queue is empty.")
        except Exception:
            print(f"Process {process_id}: Exception {traceback.format_exc()}")
