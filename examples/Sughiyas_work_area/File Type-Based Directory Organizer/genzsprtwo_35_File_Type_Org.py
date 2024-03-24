import os

def organize_files(directory):
    folder_names = {   #the mapping of file extensions to folder names
        ".jpg": "Pictures",
        ".png": "Pictures",
        ".txt": "Text",
        ".pdf": "Text",
    }

    for folder_name in set(folder_names.values()):   #create folders based on file type
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    miscellaneous_path = os.path.join(directory, "Miscellaneous") #if file type not mentioned
    if not os.path.exists(miscellaneous_path):
        os.makedirs(miscellaneous_path)

    for file_name in os.listdir(directory): #organzie the files
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower() 

            if extension in folder_names:
                folder_name = folder_names[extension]
            else:
                folder_name = "Miscellaneous"
            
            folder_path = os.path.join(directory, folder_name)
            destination_path = os.path.join(folder_path, file_name)
            os.rename(file_path, destination_path)
            print(f"Moved {file_name} to {folder_name}")

    print("All of the files have been organized")

organize_files("./Directory Organizer")
