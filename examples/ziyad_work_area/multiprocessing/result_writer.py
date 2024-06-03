import traceback
from queue import Empty
from multiprocessing import Queue


class ResultWriterProcess:
    def __init__(self, result_queue: Queue):
        self.result_queue = result_queue
        self.result_file_name = "./result.txt"

    def run(self, process_id: str):
        print(f"Process {process_id}: Running.")
        while True:
            try:
                with open(self.result_file_name, "a") as res_file:
                    res_data = self.result_queue.get(timeout=3)
                    res_file.write(f"{res_data}\n")
            except Empty:
                print(f"Process {process_id}: Result Queue is empty.")
            except Exception:
                print(traceback.format_exc())
