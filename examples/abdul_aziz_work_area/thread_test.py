import threading
import time

def background_task():
    while True:
        time.sleep(1)
        print("Background task is running")

daemon_thread = threading.Thread(target=background_task)
daemon_thread.daemon = True  # Set as a daemon thread
daemon_thread.start()

# Main program will run for a short time before exiting
time.sleep(5)
print("Main program is exiting")
