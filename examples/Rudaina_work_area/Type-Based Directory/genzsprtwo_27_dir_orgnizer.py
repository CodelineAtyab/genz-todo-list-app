import os

directory = "./dir"  # the path to the parent dir
new_txt_path = os.path.join(directory, "./Text")   # path to the Text dir inside the parent dir
new_img_path = os.path.join(directory, "./Images")  # path to the Images dir inside the parent dir
miscellaneous = os.path.join(directory, "./Miscellaneous")

files = os.listdir(directory)  # get all files from the parent dir

os.mkdir(new_txt_path)  # create a new directory for .jpg files
os.mkdir(new_img_path)  # create a new directory for .jpg files
os.mkdir(miscellaneous)  # create a new directory for other files


txt_file_num = 0
jpg_file_num = 0
miscellaneous_num = 0
for file in files:
    if file.endswith(".txt") or file.endswith(".pdf"):  # if .txt file move it to Text dir
        src = os.path.join(directory, file)
        dst = os.path.join(new_txt_path, file)
        os.rename(src, dst)
        txt_file_num += 1

    elif file.endswith(".jpg") or file.endswith(".png"):  # if its .jpg  move it to Images dir
        src = os.path.join(directory, file)
        dst = os.path.join(new_img_path, file)
        os.rename(src, dst)
        jpg_file_num += 1

    else:  # any other file move it to miscellaneous dir
        src = os.path.join(directory, file)
        dst = os.path.join(miscellaneous, file)
        os.rename(src, dst)
        miscellaneous_num += 1


print("Summary:")
print("-------")
print(f'- Moved {txt_file_num} .txt files to directory: {directory}/Text')
print(f'- Moved {jpg_file_num} .jpg files to directory: {directory}/Images')
print(f'- Moved {miscellaneous_num} other files to directory: {directory}/Miscellaneous')
