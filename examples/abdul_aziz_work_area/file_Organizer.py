import shutil
import os




parent_directory = "./dir"
image_directory = "./dir/Images"
text_directory = "./dir/Text"
miscellaneous_directory = "./dir/Miscellaneous"

for directory in [image_directory, text_directory, miscellaneous_directory]:
    if not os.path.exists(directory):
        os.makedirs(directory)

files = os.listdir(parent_directory)
for file in files:
        file_name, file_extension = os.path.splitext(file)
        if file_name in ["Images", "Text", "Miscellaneous"]:
            continue
        destination_directory = None
        if file_extension.lower() in [".jpg", ".png", ".jpeg", ".img"]:
            destination_directory = image_directory

        elif file_extension.lower() == ".txt":
            destination_directory = text_directory
            
        else:
            destination_directory = miscellaneous_directory
           

        source_path = os.path.join(parent_directory, file)
        destination_path = os.path.join(destination_directory, file)
        shutil.move(source_path, destination_path)