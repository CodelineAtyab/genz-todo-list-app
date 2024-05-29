import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CVHandler(FileSystemEventHandler):
    def __init__(self, cv_queue):
        self.cv_queue = cv_queue

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".pdf"):
            # Add new CV file to the processing queue
            self.cv_queue.put(event.src_path)
            logging.info(f"Producer: Added {event.src_path} to queue.")

def producer(cv_queue, directory_to_watch):
    event_handler = CVHandler(cv_queue)
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=False)
    observer.start()
    logging.info("Producer: Monitoring directory for new CVs.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
