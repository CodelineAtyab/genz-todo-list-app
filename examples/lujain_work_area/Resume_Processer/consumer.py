import traceback
import logging
from queue import Empty
from pyresparser import ResumeParser

def process_cv(process_id, cv_queue, res_queue):
    logging.info(f"Consumer {process_id}: Running.")
    try:
        while True:
            try:
                # Get CV file path from the queue
                cv_file_path = cv_queue.get(timeout=3)
                # Process the CV using pyresparser
                data = ResumeParser(cv_file_path).get_extracted_data()
                logging.info(f"Consumer {process_id}: Processed {cv_file_path}")
                # Put the processed data into the result queue
                res_queue.put((cv_file_path, data))
            except Empty:
                logging.info(f"Consumer {process_id}: Queue is empty.")
                break
            except Exception as e:
                logging.error(f"Consumer {process_id}: Exception {traceback.format_exc()}")
    except KeyboardInterrupt:
        logging.info(f"Consumer {process_id}: Stopping.")
