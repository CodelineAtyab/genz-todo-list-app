import os
import shutil
import glob

DIRECTORY = "./dir"


def dir_organizer(source_dir):
    new_txt_path = os.path.join(source_dir, "./Text")
    new_img_path = os.path.join(source_dir, "./Images")
    miscellaneous = os.path.join(source_dir, "./Miscellaneous")
    for directory in [new_img_path, new_txt_path, miscellaneous]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    files = glob.glob(os.path.join(source_dir, '*'))

    for file in files:
        if os.path.isfile(file):
            if file.endswith(('.txt', '.pdf')):
                shutil.move(file, os.path.join(new_txt_path, os.path.basename(file)))
            elif file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                shutil.move(file, os.path.join(new_img_path, os.path.basename(file)))
            else:
                shutil.move(file, os.path.join(miscellaneous, os.path.basename(file)))


dir_organizer(DIRECTORY)
