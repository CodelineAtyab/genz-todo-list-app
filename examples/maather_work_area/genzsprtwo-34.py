import os
_DIRECTORY = "./dir_organizer_files/"

def directory_organizer(directory):
    try:
        contents = os.listdir(_DIRECTORY)
        files = [content for content in contents if os.path.isfile(os.path.join(directory, content))]
    except OSError as e:
        print((f"error:{e}"))
        return

    for file in files:
        if file.endswith(".txt"):
            os.makedirs(_DIRECTORY + "text", exist_ok=True)
            os.rename(_DIRECTORY + file, _DIRECTORY + "text/" + file )
        elif file.endswith(".img", ".png", ".jpeg"):
            os.makedirs(_DIRECTORY + "images", exist_ok=True)
            os.rename(_DIRECTORY + file, _DIRECTORY + "images/" + file )
        else:
            os.makedirs(_DIRECTORY + "misc", exist_ok=True)
            os.rename(_DIRECTORY + file, _DIRECTORY + "misc/" + file )


directory_organizer(_DIRECTORY)

