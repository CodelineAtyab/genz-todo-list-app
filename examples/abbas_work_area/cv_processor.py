import glob
import traceback
import time

from queue import Empty
from multiprocessing import Process, Queue

from pyresparser import ResumeParser

from cv_consumer import CVConsumer


if __name__ == "__main__":
    main_cv_file_queue = Queue(maxsize=0)
    result_skills_queue = Queue(maxsize=0)
    no_of_consumer_processes = 2  # Utilize all CPU cores
    consumer = CVConsumer()

    """
    Producer Implementation START
    """
    # Producer - Lets put all the CVs in the Queue
    list_of_uploaded_cvs = glob.glob("./Documents/uploads/*.pdf")

    for curr_cv_file_path in list_of_uploaded_cvs:
        main_cv_file_queue.put(curr_cv_file_path)
    """
    Producer Implementation END
    """

    """
    Result Consumer START
    """
    res_consumer_process = Process(target=consumer.write_result_to_file, args=("res_con", result_skills_queue))
    res_consumer_process.start()
    """
    Result Consumer END
    """

    list_of_consumer_processes = []
    for pid in range(1, no_of_consumer_processes+1):
        curr_process = Process(target=consumer.process_cv, args=(str(pid), main_cv_file_queue, result_skills_queue))
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
