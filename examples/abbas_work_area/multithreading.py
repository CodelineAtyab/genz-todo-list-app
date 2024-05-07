import time
import threading


def display_time():
    try:
        while True:
            print(time.time())
            time.sleep(1)
    except Exception as ex:
        print("Error", ex)


if __name__ == "__main__":
    try:
        background_thread = threading.Thread(target=display_time)
        background_thread.daemon = True
        background_thread.start()
    except Exception as ex:
        print("Error", ex)

    msg = input("Enter a msg: ")
