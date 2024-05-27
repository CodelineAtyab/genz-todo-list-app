from queue import Queue  # Thread-safe

import requests
from pyresparser import ResumeParser


# I/O bound task - Consumer
def get_profile_info_from_github(name):
    print(f"Fetching github profile info for {name}")
    res = requests.get(f"https://api.github.com/users/{name}")
    res_dict = res.json()

    res = requests.get(res_dict["repos_url"])
    res_list = res.json()
    print(res_list[0]["description"])


# CPU Bound tasks
def process_cv(inc_cv_file_path, res_queue: Queue) -> None:
    print(f"Starting processing the CV file {inc_cv_file_path}")
    start_time = time.time()
    res_queue.put(ResumeParser(inc_cv_file_path).get_extracted_data())
    processing_time = time.time() - start_time
    print(f'it took {processing_time} seconds to parse the CV.')


if __name__ == "__main__":
    # TODO (genz-1234): We are using Outlook API to read emails having subjects, body and attachment
    attached_file = "multi_threading/CSExampleResume1.pdf"
    # attached_file_2 = "./ziyad_cv.pdf"
    linkedin_profile_name = "HaithamAlMaamari"
    result_queue = Queue()

    child_thread_1 = threading.Thread(target=process_cv, args=tuple([attached_file, result_queue]))
    child_thread_1.daemon = True

    # child_thread_4 = threading.Thread(target=process_cv, args=tuple([attached_file_2, result_queue]))
    # child_thread_4.daemon = True

    child_thread_2 = threading.Thread(target=get_profile_info_from_github, args=("HaithamAlMaamari",))
    child_thread_2.daemon = True

    child_thread_3 = threading.Thread(target=get_profile_info_from_github, args=("aaziz9",))
    child_thread_3.daemon = True

    child_thread_1.start()
    child_thread_2.start()
    child_thread_3.start()
    # child_thread_4.start()

    child_thread_1.join()
    child_thread_2.join()
    child_thread_3.join()

    while not result_queue.empty():
        print(result_queue.get())
