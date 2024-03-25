import os
import shutil
import glob

_DIRECTORY = "./dir_organizer_files/"

def directory_organizer(directory):
    try:
        files = glob.glob(os.path.join(directory, "*"))
    except OSError as e:
        print(f"error: {e}")
        return

    for file in files:
        if os.path.isfile(file):
            if file.endswith(".txt"):
                destination = os.path.join(directory, "text")
            elif file.endswith((".img", ".png", ".jpeg")):
                destination = os.path.join(directory, "images")
            else:
                destination = os.path.join(directory, "misc")

            os.makedirs(destination, exist_ok=True)
            shutil.move(file, os.path.join(destination, os.path.basename(file)))


directory_organizer(_DIRECTORY)
