import time
import threading


def disp_time():
    try:
        while True:
            print(time.time())
            time.sleep(1)
    except Exception as excep:
        print("Error", excep)


if __name__ == "__main__":
    try:
        background_thread = threading.Thread(target=disp_time)
        background_thread.daemon = True
        background_thread.start()
    except Exception as excep:
        print("Error", excep)

    text = input("Text: ")
