import time
import threading


def print_time():
    while True:
        print(time.time())
        time.sleep(1)


if __name__ == "__main__":
    try:
        bg_thread = threading.Thread(target=print_time)
        bg_thread.daemon = True
        bg_thread.start()
    except Exception as ex:
        print("An error occurred: ", ex)

    user_input = input("Type your message: ")
