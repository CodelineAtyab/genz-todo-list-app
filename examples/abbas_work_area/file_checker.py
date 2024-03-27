"""
This program identifies what files exist in Directory folder,
and splits them into their relevant folders based on their extension
"""

import os
import shutil

directory = "./dir"
text_path = './dir/Text'
image_path = './dir/Image'
miscellaneous_path = './dir/Misc'

# Checking if folders exist, if not it creates them
if not os.path.exists(image_path):
    os.mkdir(image_path)
elif not os.path.exists(text_path):
    os.mkdir(text_path)
elif not os.path.exists(miscellaneous_path):
    os.mkdir(miscellaneous_path)

# Reads all files in main directory
files = os.listdir(directory)

# initialize a count of files moved
image = 0
misc = 0
text = 0

# Moves the files to the folders that they belong to
for file in files:
    origin = os.path.join(directory, file)
    if os.path.isfile(origin):
        if file.endswith('.jpg') or file.endswith('.png'):
            destination = os.path.join(image_path, file)
            shutil.move(origin, destination)
            image = image + 1
        elif file.endswith('.txt') or file.endswith('.pdf'):
            destination = os.path.join(text_path, file)
            shutil.move(origin, destination)
            text = text + 1
        else:
            destination = os.path.join(miscellaneous_path, file)
            shutil.move(origin, destination)
            misc = misc + 1

print(f"Files in Directory: {os.listdir(image_path)}, Number of Files Moved: {image}")
print(f"Files in Directory: {os.listdir(text_path)}, Number of Files Moved: {text}")
print(f"Files in Directory: {os.listdir(miscellaneous_path)}, Number of Files Moved: {misc}")
