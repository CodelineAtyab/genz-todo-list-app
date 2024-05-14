import multiprocessing
import time


def sum_squares(task_id, queue):
    try:
        start = time.time()
        result = sum(i ** 2 for i in range(10000))
        queue.put((task_id, "squares", result, time.time() - start))
    except Exception as ex:
        print(f"{task_id}", ex)


def sum_cubes(task_id, queue):
    try:
        start = time.time()
        result = sum(i ** 3 for i in range(10000))
        queue.put((task_id, "cubes", result, time.time() - start))
    except Exception as ex:
        print(f"{task_id}", ex)


def main():
    num_process = 2
    queue = multiprocessing.Queue()
    process = []

    start = time.time()

    for i in range(num_process):
        if i % 2 == 0:
            calc = multiprocessing.Process(target=sum_squares, args=(i, queue))
        else:
            calc = multiprocessing.Process(target=sum_cubes, args=(i, queue))
        process.append(calc)
        calc.start()

    for calc in process:
        calc.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    for result in results:
        task_id, task_type, value, elapsed_time = result
        print(f"Task type: {task_type}. Result: {value}. time Taken: {elapsed_time:.3f} ")

    print(f"process complete. Time Taken: {time.time() - start:.3f}")


if __name__ == "__main__":
    main()
