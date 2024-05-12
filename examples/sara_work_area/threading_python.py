import time
import threading


# Function to print time
def print_time():
    while True:
        print(time.time())
        time.sleep(1)


# Function to print counter
def display_counter():
    count = 0
    while count < 10:
        print(count)
        count += 1


if __name__ == "__main__":
    try:
        # Thread to print time
        time_thread = threading.Thread(target=print_time)
        time_thread.daemon = True
        time_thread.start()

        # Thread to display counter
        counter_thread = threading.Thread(target=display_counter)
        counter_thread.daemon = True
        counter_thread.start()

        # Wait only for the counter thread to complete execution
        counter_thread.join()

    except Exception as ex:
        print("An error occurred: ", ex)

    print("Thank you!")
