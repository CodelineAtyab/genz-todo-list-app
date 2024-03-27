import os
import shutil

_DIRECTORY = "./dir_organizer_files/"

def directory_organizer(directory):
    try:
        contents = os.listdir(directory)
        files = [content for content in contents if os.path.isfile(os.path.join(directory, content))]
    except OSError as e:
        print(f"error: {e}")
        return

    for file in files:
        if file.endswith(".txt"):
            target_dir = os.path.join(directory, "text")
        elif file.endswith((".img", ".png", ".jpeg")):
            target_dir = os.path.join(directory, "images")
        else:
            target_dir = os.path.join(directory, "misc")
        
        os.makedirs(target_dir, exist_ok=True)
        shutil.move(os.path.join(directory, file), os.path.join(target_dir, file))

directory_organizer(_DIRECTORY)