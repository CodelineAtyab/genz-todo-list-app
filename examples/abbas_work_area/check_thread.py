import time
import threading
import glob
import os
import hashlib
import json


directory = "./multithreading/*"
content_lock = threading.Lock()
content = []
data_store = "./data/data.json"
existing_hashes = set()


def process_file(file_path, data="", state="r"):
    """
    :param file_path: contains the file path used to store or read.
    :param data: any data that needs to be appended to file.
    :param state: whether to open file in append or read mode.
    :return: returns read file for processing.
    """

    with open(file_path, state) as store_file:
        if state == "a":
            store_file.write(data)
        elif state == "r":
            return store_file.read()


def get_existing_hashes():
    """
    :return: gets and returns existing hashes.
    """
    file_content = process_file(data_store)
    if file_content:
        for line in file_content.splitlines():
            store_entry = json.loads(line)
            existing_hashes.add(store_entry['hash'])
        return existing_hashes


def is_empty(path):
    """
    :param path: contains the file path.
    :return: returns if the path is empty.
    """

    files = glob.glob(path)
    return len(files) == 0


def check_dir():
    """
    :return: if directory not empty call check_if_read function.
    """
    while True:
        if not is_empty(directory):
            check_if_read()
        time.sleep(2)


def check_if_read():
    """
    checks if file has been read and processed before or not based on its hash code.
    :return:
    """
    files = glob.glob(directory)
    for file_path in files:
        value = process_file(file_path)
        if value:
            data_hash = hashlib.sha256(value.encode()).hexdigest()
            if data_hash not in existing_hashes:
                read_str(file_path)
            else:
                pass


def read_str(file_path):
    """
    :param file_path: contains the file path
    :return: retrieves data once called, and sends it to be appended by append_value
    """
    value = process_file(file_path)
    append_value(value, file_path)


def append_value(data, file_path):
    """
    appends, data, hash code, and filename to storage file.
    :param data: data to appended
    :param file_path: contains the file path
    :return:
    """
    data_hash = hashlib.sha256(data.encode()).hexdigest()
    filename = os.path.basename(file_path)
    store_entry = {'data': data, 'hash': data_hash, "filename": filename}
    with content_lock:
        content.append(data)
        existing_hashes.add(data_hash)
    process_file(data_store, json.dumps(store_entry) + "\n", 'a')


def count_chars():
    """
    counts how many "a" are in the read string.
    :return:
    """
    while True:
        with content_lock:
            for file_content in content:
                print(f"Number of 'a' characters: {file_content.count('a')}")
            content.clear()
        time.sleep(2)


if __name__ == "__main__":
    get_existing_hashes()

    thread1 = threading.Thread(target=check_dir)
    thread1.daemon = True

    thread2 = threading.Thread(target=count_chars)
    thread2.daemon = True

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


