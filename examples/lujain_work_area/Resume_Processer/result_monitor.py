import os
import json
import hashlib
import logging
from queue import Empty

def get_unique_filename(base_path, original_name):
    name, ext = os.path.splitext(original_name)
    counter = 1
    unique_name = f"{name}{ext}"
    # Ensure unique filename by checking existing files
    while os.path.exists(os.path.join(base_path, unique_name)):
        unique_name = f"{name}_{counter}{ext}"
        counter += 1
    return unique_name

def write_result_to_file(process_id, res_queue, result_dir):
    logging.info(f"Result Monitor {process_id}: Running.")
    os.makedirs(result_dir, exist_ok=True)

    try:
        while True:
            try:
                # Get processed result from the result queue
                cv_file_path, data = res_queue.get(timeout=3)
                
                # Read the file to compute hash for unique filename
                with open(cv_file_path, 'rb') as file:
                    file_content = file.read()
                hash_value = hashlib.sha256(file_content).hexdigest()
                
                unique_filename = get_unique_filename(result_dir, f"{hash_value}.json")

                # Write the result data to a JSON file
                with open(os.path.join(result_dir, unique_filename), "w") as res_file:
                    json.dump(data, res_file)
                logging.info(f"Result Monitor {process_id}: Wrote result for {cv_file_path} to {unique_filename}")
            except Empty:
                logging.info(f"Result Monitor {process_id}: Result Queue is empty.")
                break
            except Exception as e:
                logging.error(f"Result Monitor {process_id}: Exception {traceback.format_exc()}")
    except KeyboardInterrupt:
        logging.info(f"Result Monitor {process_id}: Stopping.")
