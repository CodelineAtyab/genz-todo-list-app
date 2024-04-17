import time


def calc_time(inp_func):
    def wrapper_func(*args):  # Accept any number of args
        start_time = time.time() # Epoch time
        ret_val = inp_func(*args)  # Unpack the collection
        print(time.time() - start_time)
        return ret_val

    return wrapper_func


@calc_time
def no_of_vowels_in_a_file(file_path):
    # Time taken to parse the file
    time.sleep(3)
    # After your logic is done with the file
    return 121


@calc_time
def a_useless_func():
    return None

print(no_of_vowels_in_a_file("./somefile.txt"))
a_useless_func()