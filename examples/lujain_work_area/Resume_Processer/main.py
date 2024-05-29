import logging
from multiprocessing import Process, Queue
from producer import producer
from consumer import process_cv
from result_monitor import write_result_to_file

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Queues for communication between processes
    main_cv_file_queue = Queue()
    result_skills_queue = Queue()
    
    # Number of consumer processes
    no_of_consumer_processes = 6

    # Directory to watch for new CV files
    directory_to_watch = "./uploads"
    result_directory = "./results"

    # Start producer process (1 core)
    producer_process = Process(target=producer, args=(main_cv_file_queue, directory_to_watch))
    producer_process.start()

    # Start consumer processes (6 cores)
    consumer_processes = []
    for i in range(no_of_consumer_processes):
        p = Process(target=process_cv, args=(f"Consumer-{i+1}", main_cv_file_queue, result_skills_queue))
        consumer_processes.append(p)
        p.start()

    # Start result monitor process (1 core)
    result_monitor_process = Process(target=write_result_to_file, args=("ResultMonitor", result_skills_queue, result_directory))
    result_monitor_process.start()

    try:
        # Wait for all processes to finish
        producer_process.join()
        for p in consumer_processes:
            p.join()
        result_monitor_process.join()
    except KeyboardInterrupt:
        logging.info("Main: Interrupted, terminating processes.")
        # Terminate all processes on interruption
        producer_process.terminate()
        for p in consumer_processes:
            p.terminate()
        result_monitor_process.terminate()

        producer_process.join()
        for p in consumer_processes:
            p.join()
        result_monitor_process.join()
