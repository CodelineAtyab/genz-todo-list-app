import threading
import random
import time

# Function to print random numbers
def print_random_numbers():
    for _ in range(5):
        print(random.randint(1, 100))
        time.sleep(1)

# Function for countdown timer
def countdown_timer():
    for i in range(5, 0, -1):
        print("Countdown:", i)
        time.sleep(1)

if __name__ == "__main__":
    try:
        # Create a thread for printing random numbers
        random_thread = threading.Thread(target=print_random_numbers)
        random_thread.daemon = True  # Set the thread as daemon
        random_thread.start()  # Start the thread

        # Create a thread for the countdown timer
        timer_thread = threading.Thread(target=countdown_timer)
        timer_thread.daemon = True  # Set the thread as daemon
        timer_thread.start()  # Start the thread
    except Exception as ex:
        print("An error occurred: ", ex)

    # Wait for both threads to finish before printing final message
    random_thread.join()
    timer_thread.join()

    print("Threads have finished executing.")