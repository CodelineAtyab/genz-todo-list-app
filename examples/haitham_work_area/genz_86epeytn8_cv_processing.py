import glob
import traceback
import time

from queue import Empty
from multiprocessing import Process, Queue

from pyresparser import ResumeParser


class CVProducer:
    def __init__(self, cv_queue: Queue, directory: str):
        self.cv_queue = cv_queue
        self.directory = directory

    def load_cvs(self):
        list_of_uploaded_cvs = glob.glob(f"{self.directory}/*.pdf")
        for curr_cv_file_path in list_of_uploaded_cvs:
            self.cv_queue.put(curr_cv_file_path)
        print(f"Producer: Loaded {len(list_of_uploaded_cvs)} CVs into the queue.")


class CVConsumer:
    def __init__(self, process_id: str, cv_queue: Queue, res_queue: Queue):
        self.process_id = process_id
        self.cv_queue = cv_queue
        self.res_queue = res_queue

    def process_cv(self):
        print(f"Process {self.process_id}: Running.")
        try:
            while not self.cv_queue.empty():
                cv_file_path = self.cv_queue.get(timeout=3)
                data = ResumeParser(cv_file_path).get_extracted_data()
                print(f"Process {self.process_id}: Data: {data}")
                self.res_queue.put(data)
        except Empty:
            print(f"Process {self.process_id}: Queue is empty.")
        except Exception:
            print(f"Process {self.process_id}: Exception {traceback.format_exc()}")


class ResultWriter:
    def __init__(self, process_id: str, res_queue: Queue, result_file: str = "./result.txt"):
        self.process_id = process_id
        self.res_queue = res_queue
        self.result_file = result_file

    def write_result_to_file(self):
        print(f"Process {self.process_id}: Running.")
        while True:
            try:
                with open(self.result_file, "a") as res_file:
                    res_data = self.res_queue.get(timeout=3)
                    res_file.write(f"{res_data}\n")
            except Empty:
                print(f"Process {self.process_id}: Result Queue is empty.")
                break
            except Exception:
                print(traceback.format_exc())


if __name__ == "__main__":
    main_cv_file_queue = Queue(maxsize=0)
    result_skills_queue = Queue(maxsize=0)
    no_of_consumer_processes = 7  # Utilize all CPU cores

    producer = CVProducer(main_cv_file_queue, "./uploads/*")
    producer.load_cvs()

    res_consumer_process = Process(target=ResultWriter("res_con", result_skills_queue).write_result_to_file)
    res_consumer_process.start()

    list_of_consumer_processes = []
    for pid in range(1, no_of_consumer_processes + 1):
        consumer = CVConsumer(str(pid), main_cv_file_queue, result_skills_queue)
        curr_process = Process(target=consumer.process_cv)
        list_of_consumer_processes.append(curr_process)
        curr_process.start()

    time.sleep(3)

    print("Assuming all consumer processes are waiting now")

    start_time = time.time()

    for curr_consumer_process in list_of_consumer_processes:
        while curr_consumer_process.is_alive():
            curr_consumer_process.join(timeout=1)

    print(f"Time it took to process CVs: {time.time() - start_time}")

    res_consumer_process.join()

    print("Exiting ...")
