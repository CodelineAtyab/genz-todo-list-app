import time
import threading

import requests
from pyresparser import ResumeParser


# I/O bound task
def get_profile_info_from_github(name):
    print(f"Fetching github profile info for {name}")
    res = requests.get(f"https://api.github.com/users/{name}")
    res_dict = res.json()

    res = requests.get(res_dict["repos_url"])
    res_list = res.json()
    print(res_list[0]["description"])


# CPU Bound tasks
def process_cv():
    print("Starting processing the CV")
    start_time = time.time()
    data = ResumeParser('atyab_cv.pdf').get_extracted_data()
    processing_time = time.time() - start_time
    print(data)
    print(f'it took {processing_time} seconds to parse the CV.')


if __name__ == "__main__":
    child_thread_1 = threading.Thread(target=process_cv)
    child_thread_1.daemon = True

    child_thread_2 = threading.Thread(target=get_profile_info_from_github, args=("HaithamAlMaamari",))
    child_thread_2.daemon = True

    child_thread_3 = threading.Thread(target=get_profile_info_from_github, args=("aaziz9",))
    child_thread_3.daemon = True

    child_thread_1.start()
    child_thread_2.start()
    child_thread_3.start()

    child_thread_1.join()
    child_thread_2.join()
    child_thread_3.join()

