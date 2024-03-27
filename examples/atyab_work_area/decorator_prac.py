import time

def profiler(inc_func):
    def wrapper(*arg, **kwargs):

        start_time = time.time()
        ret_val = inc_func(*arg, **kwargs)
        end_time = time.time() - start_time
        print(f"Execution time in sec {end_time}")
        return "<h1>" + ret_val + "</h1>"

    return wrapper

@profiler
def f1(name, year, status="UNKNOWN"):
    time.sleep(1)
    return "Hello " + name + str(year) + " " + status


print(f1("GenZ", 2024))