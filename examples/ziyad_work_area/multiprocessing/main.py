import glob
import time
from multiprocessing import Queue, Process
from queue import Empty
from resume_parser import ResumeParserProcess
from result_writer import ResultWriterProcess


class CVProcessor:
    def __init__(self, cv_directory: str, num_consumers: int):
        self.cv_directory = cv_directory
        self.num_consumers = num_consumers
        self.cv_queue = Queue(maxsize=0)
        self.result_queue = Queue(maxsize=0)

    def load_cvs(self):
        list_of_uploaded_cvs = glob.glob(f"{self.cv_directory}/*.pdf")
        for cv in list_of_uploaded_cvs:
            self.cv_queue.put(cv)

    def start_processes(self):
        self.result_writer_process = Process(target=ResultWriterProcess(self.result_queue).run, args=("res_con",))
        self.result_writer_process.start()

        self.consumer_processes = [
            Process(target=ResumeParserProcess(self.cv_queue, self.result_queue).run, args=(str(pid),))
            for pid in range(1, self.num_consumers + 1)
        ]

        for process in self.consumer_processes:
            process.start()

    def join_processes(self):
        for process in self.consumer_processes:
            while process.is_alive():
                process.join(timeout=1)

        self.result_writer_process.join()

    def run(self):
        self.load_cvs()
        self.start_processes()
        start_time = time.time()

        print("Assuming all consumer processes are waiting now")

        self.join_processes()

        print(f"Time it took to process CVs: {time.time() - start_time:.2f} seconds")
        print("Exiting...")


if __name__ == "__main__":
    cv_processor = CVProcessor(cv_directory="./uploads", num_consumers=7)
    cv_processor.run()
