import os
import shutil
import glob

folders = {
        'jpg': 'Images',
        'jpeg': 'Images',
        'png': 'Images',
        'txt': 'Text',
        'pdf': 'Documents',
    }


def organize_files(folder):

    moved_files = 0
    folder_created = set()

    for ext, dest_folder in folders.items():
        full_path = os.path.join(folder, dest_folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            folder_created.add(dest_folder)

        for file in glob.glob(folder + f'/*.{ext}'):
            shutil.move(file, full_path)
            moved_files += 1

    misc_folder = os.path.join(folder, 'Miscellaneous')
    if not os.path.exists(misc_folder):
        os.makedirs(misc_folder)
        folder_created.add('Miscellaneous')

    for file in glob.glob(folder + '/*'):
        if os.path.isfile(file) and not any(file.endswith('.' + e) for e in folders):
            shutil.move(file, misc_folder)
            moved_files += 1

    print(f"Moved {moved_files} files.")
    if folder_created:
        print("Created folders:", ", ".join(folder_created))
    else:
        print("No new folders were created.")


path_to_organize = '/dir'
organize_files(path_to_organize)
