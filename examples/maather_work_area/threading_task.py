import threading
import time


def task1():
    print("Task 1 started")
    time.sleep(3) 
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2) 
    print("Task 2 completed")

def main():
    # Create threads for each task
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    # Start the threads
    thread1.start()
    thread2.start()

    # Main program continues executing
    print("Main program continues...")

    # Wait for the threads to complete
    thread1.join() 
    thread2.join() 

    print("All tasks completed")

if __name__ == "__main__":
    main()
