import os
import shutil

DIRECTORY = "./File_Directory"

def organize_files(directory):
    file_types = {
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images',
        '.gif': 'Images', '.bmp': 'Images', '.tiff': 'Images',
        '.txt': 'Text', '.pdf': 'PDF'
    }
    default_dir = 'Miscellaneous'
    
    # Creates subdirectories if they don't exist
    for dir_name in set(file_types.values()) | {default_dir}:
        os.makedirs(os.path.join(directory, dir_name), exist_ok=True)

    files_moved_count = {directory_name: 0 for directory_name in set(file_types.values()) | {default_dir}}

    # Filters out already organized files
    organized_files = set(os.listdir(os.path.join(directory, default_dir)))
    for file_type in file_types.values():
        organized_files |= set(os.listdir(os.path.join(directory, file_type)))

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and filename not in organized_files:
            file_extension = os.path.splitext(filename)[1].lower()
            destination_directory = file_types.get(file_extension, default_dir)
            destination_path = os.path.join(directory, destination_directory, filename)
            shutil.move(os.path.join(directory, filename), destination_path)
            files_moved_count[destination_directory] += 1

    print("Organized files successfully.")
    for directory, count in files_moved_count.items():
        print(f"{count} files moved to {directory}")


organize_files(DIRECTORY)
import os
import shutil

DIRECTORY = "./File_Directory"

def create_directories(directory, file_types):
    # Creates subdirectories if they don't exist
    for dir_name in set(file_types.values()) | {'Miscellaneous'}:
        os.makedirs(os.path.join(directory, dir_name), exist_ok=True)

def organize_files(directory, file_types):
    default_dir = 'Miscellaneous'

    files_moved_count = {directory_name: 0 for directory_name in set(file_types.values()) | {default_dir}}

    # Filters out already organized files
    organized_files = set(os.listdir(os.path.join(directory, default_dir)))
    for file_type in file_types.values():
        organized_files |= set(os.listdir(os.path.join(directory, file_type)))

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and filename not in organized_files:
            file_extension = os.path.splitext(filename)[1].lower()
            destination_directory = file_types.get(file_extension, default_dir)
            destination_path = os.path.join(directory, destination_directory, filename)
            shutil.move(os.path.join(directory, filename), destination_path)
            files_moved_count[destination_directory] += 1

    print("Organized files successfully.")
    for directory, count in files_moved_count.items():
        print(f"{count} files moved to {directory}")

def organize_files_and_create_dirs(directory):
    file_types = {
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images',
        '.gif': 'Images', '.bmp': 'Images', '.tiff': 'Images',
        '.txt': 'Text', '.pdf': 'PDF'
    }

    # Call to create_directories function
    create_directories(directory, file_types)

    # Call to organize_files function
    organize_files(directory, file_types)

# Call to the combined function to perform both tasks
organize_files_and_create_dirs(DIRECTORY)
