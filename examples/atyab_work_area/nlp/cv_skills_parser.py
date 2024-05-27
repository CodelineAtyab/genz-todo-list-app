import time
from pyresparser import ResumeParser

start_time = time.time()
data = ResumeParser('atyab_cv.pdf').get_extracted_data()
processing_time = time.time() - start_time
print(data)
print(f'it took {processing_time} seconds to parse the CV.')

my_message = input("Enter your message:")

# Get message from Ziyads process
inc_msg = "I am fine"
print(f"Ziyad: {inc_msg}")