import os

"""
A program to organize files into directories
based on their extensions 
"""

parent_directory = "./dir"
image_directory = "./dir/Images"
text_directory = "./dir/Text"
miscellaneous_directory = "./dir/Miscellaneous"

for directory in [image_directory, text_directory, miscellaneous_directory]:
    if not os.path.exists(directory):
        os.makedirs(directory)


try:
    no_of_img_files, no_of_txt_files, no_of_misc_files = 0, 0, 0
    files = os.listdir(parent_directory)
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        # print(f"File: {file}, Extension: {file_extension}")
        if file_name in ["Images", "Text", "Miscellaneous"]:
            continue
        destination_directory = None
        if file_extension.lower() in [".jpg", ".png", ".jpeg", ".img"]:
            destination_directory = image_directory
            no_of_img_files += 1
        elif file_extension.lower() == ".txt":
            destination_directory = text_directory
            no_of_txt_files += 1
        else:
            destination_directory = miscellaneous_directory
            no_of_misc_files += 1

        new_file_path = os.path.join(destination_directory, file)
        os.rename(os.path.join(parent_directory, file), new_file_path)
    print(f"The number of image files moved is {no_of_img_files}\nThe number of text files moved is {no_of_txt_files}\nThe number of miscellaneous files moved is {no_of_misc_files}")

except FileNotFoundError:
    print("Unable to find directory:", parent_directory)
except Exception as ex:
    print("Something went wrong.", ex)