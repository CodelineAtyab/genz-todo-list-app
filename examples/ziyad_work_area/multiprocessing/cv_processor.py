"""
    In the previous example, we observed the following:
    - Main thread took 44.2 seconds to process all 30 CVs
    - Multiple threads 52 seconds to parse all 30 CVs
    - Multiple processes 21.11 to parse 30 CVS

    Producer Consumer Architecture
"""
import glob
import traceback
import time

from queue import Empty
from multiprocessing import Process, Queue

from pyresparser import ResumeParser


def process_cv(process_id: str, cv_queue: Queue, res_queue: Queue):
    print(f"Process {process_id}: Running.")

    try:
        while not cv_queue.empty():
            cv_file_path = cv_queue.get(timeout=3)
            data = ResumeParser(cv_file_path).get_extracted_data()
            print(f"Process {process_id}: Data: {data}")
            res_queue.put(data)
    except Empty:
        print(f"Process {process_id}: Queue is empty.")
    except Exception:
        print(f"Process {process_id}: Exception {traceback.format_exc()}")


def write_result_to_file(process_id, res_queue: Queue):
    """
    Consume the result Queue and save the skills to a file
    :param res_queue: TBD
    :param process_id: Identifier for this process
    :return:
    """
    print(f"Process {process_id}: Running.")
    result_file_name = "./result.txt"
    while True:
        try:
            with open(result_file_name, "a") as res_file:
                res_data = res_queue.get(timeout=3)
                res_file.write(f"{res_data}\n")
        except Empty:
            print(f"Process {process_id}: Result Queue is empty.")
        except Exception:
            print(traceback.format_exc())


if __name__ == "__main__":
    main_cv_file_queue = Queue(maxsize=0)
    result_skills_queue = Queue(maxsize=0)
    no_of_consumer_processes = 7  # Utilize all CPU cores

    """
    Producer Implementation START
    """
    # Producer - Lets put all the CVs in the Queue
    list_of_uploaded_cvs: list[str] = glob.glob("./uploads/*.pdf")

    for curr_cv_file_path in list_of_uploaded_cvs:
        main_cv_file_queue.put(curr_cv_file_path)
    """
    Producer Implementation END
    """

    """
    Result Consumer START
    """
    res_consumer_process = Process(target=write_result_to_file, args=("res_con", result_skills_queue))
    res_consumer_process.start()
    """
    Result Consumer END
    """

    list_of_consumer_processes: list[Process] = []
    for pid in range(1, no_of_consumer_processes+1):
        curr_process = Process(target=process_cv, args=(str(pid), main_cv_file_queue, result_skills_queue))
        list_of_consumer_processes.append(curr_process)
        curr_process.start()

    time.sleep(3)

    print("Assuming all consumer processes are waiting now")

    start_time = time.time()

    # All consumer processes are waiting at this point
    for curr_consumer_process in list_of_consumer_processes:
        while curr_consumer_process.is_alive():
            curr_consumer_process.join(timeout=1)

    print(f"Time it took to process 30 CVs {time.time() - start_time}")

    res_consumer_process.join()

    print("Exiting ...")