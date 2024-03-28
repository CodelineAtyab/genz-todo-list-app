import hashlib


def create_hash(filename):
    try:
        with open(filename, 'rb') as file:  # read
            file_content = file.read()

        hash_result = hashlib.sha256(file_content).hexdigest()  # generate sha256

        hash_filename = filename + '.sha256'
        with open(hash_filename, 'w') as hash_file:
            hash_file.write(hash_result)

        print("Hash created and saved.")
    except IOError as error:
        print(f"Couldn't read or write files: {error}")


def check_file(filename):
    hash_filename = filename + '.sha256'

    try:
        with open(hash_filename, 'r') as hash_file:
            saved_hash = hash_file.read().strip()

        with open(filename, 'rb') as file:
            file_content = file.read()
        current_hash = hashlib.sha256(file_content).hexdigest()

        if current_hash == saved_hash:
            print("File is unchanged.")
        else:
            print("File has been altered!")
    except IOError as error:
        print(f"Error: {error}")

# To use the script:
# To create a hash for 'yourfile.txt', use:
# create_hash('yourfile.txt')

# To check if 'yourfile.txt' is unchanged, use:
# check_file('yourfile.txt')