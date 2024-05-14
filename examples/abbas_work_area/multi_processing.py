"""
This program looks into multiprocessing, where it processes sum of squares and sum of cubes
at the same time.
"""

import multiprocessing
import time


def sum_squares(task_id, queue):
    """
    :param task_id: contains ID of task
    :param queue: adds process to queue
    :return: returns the processed sum squares.
    """
    try:
        start = time.time()
        result = sum(i ** 2 for i in range(10000))
        queue.put((task_id, "squares", result, time.time() - start))
    except Exception as ex:
        print(f"{task_id}", ex)


def sum_cubes(task_id, queue):
    """
    :param task_id: ID of the task
    :param queue: put process into a queue to handle multiprocessing
    :return: the processed data is added to a queue to be handled at the same time.
    """
    try:
        start = time.time()
        result = sum(i ** 3 for i in range(10000))
        queue.put((task_id, "cubes", result, time.time() - start))
    except Exception as ex:
        print(f"{task_id}", ex)


def main():
    """
    contains logic to handle multiprocessing
    :return:
    """
    num_process = 7  # Number of times the process should run
    queue = multiprocessing.Queue()
    process = []

    start = time.time()  # Start timer to count time for the entir process to complete

    for i in range(num_process):  # Split the processing between the two functions
        if i % 2 == 0:
            calc = multiprocessing.Process(target=sum_squares, args=(i, queue))  # processing sum squares
        else:
            calc = multiprocessing.Process(target=sum_cubes, args=(i, queue))  # processing sum cubes
        process.append(calc)
        calc.start()

    for calc in process:  # Makes sure the process waits for all processes
        calc.join()

    results = []
    while not queue.empty():  # Append results from queue
        results.append(queue.get())

    for result in results:  # Print all results
        task_id, task_type, value, elapsed_time = result
        print(f"Task type: {task_type}. Result: {value}. time Taken: {elapsed_time:.3f} ")

    print(f"process complete. Time Taken: {time.time() - start:.3f}")


if __name__ == "__main__":
    main()
