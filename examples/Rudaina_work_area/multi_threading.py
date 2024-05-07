import threading
import requests


def fetch_github_profile(name):
    try:
        print(f"Fetching github profile info for {name}")
        res = requests.get(f"https://api.github.com/users/{name}")
        res_dict = res.json()
        print("Task 1 completed fetch github profile")
    except Exception as ex:
        print("An error occurred in task1:", ex)

def write_to_file(data):
    try:
        with open("github_profile.txt", "w") as file:
            file.write("{'login': 'Rudainasaleh', 'id': 79608302}")
        print("Task 2 completed writing to file.")
    except Exception as ex:
        print("An error occurred in task2:", ex)

def read_from_file():
    try:
        with open("github_profile.txt", "r") as file:
            data = file.read()
        print("Data read from file:", data)
        print("Task 3 completed writing to file.")
    except Exception as ex:
        print("An error occurred in task3:", ex)

if __name__ == "__main__":
    try:

        t1 = threading.Thread(target=fetch_github_profile, args=("Rudainasaleh",))

        # Task 2: Write profile data to file
        t2 = threading.Thread(target=write_to_file, args=(t1,))


        # Task 3: Read profile data from file
        t3 = threading.Thread(target=read_from_file)

        t1.start()
        t1.join()

        t2.start()
        t3.start()

        t2.join()
        t3.join()

    except Exception as ex:
        print("An error occurred in the main program:", ex)
