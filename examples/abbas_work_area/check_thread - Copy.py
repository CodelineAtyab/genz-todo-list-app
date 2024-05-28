import time
import threading
import os
import glob

directory = "./multithreading/*"
content_lock = threading.Lock()
content = []

def is_empty(path)
