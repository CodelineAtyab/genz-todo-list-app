import hashlib


def generate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, 'rb') as input_file:
        for blocks in iter(lambda: input_file.read(4096), b""):
            sha256.update(blocks)
    return sha256.hexdigest()


def store_sha256(file_path):
    sha256_code = generate_sha256(file_path)
    try:
        with open(file_path + '.sha256', 'w') as store_file:
            store_file.write(sha256_code)
    except Exception as ex:
        print("Error", ex)


def check_file_integrity(file_path):
    original = ""
    with open(file_path, 'r') as read_file:
        original = read_file.read()

    new_file_path = input("Enter file path of new: ")
    new_sha256 = generate_sha256(new_file_path)

    if original == new_sha256:
        return "File Integrity True"
    else:
        return "File integrity False"


def main():
    choice = input("Enter generate or or verify: ")
    file_path = input("Enter the file path: ")

    if choice.lower().strip() == "generate":
        store_sha256(file_path)
    elif choice.lower().strip() == "verify":
        print(check_file_integrity(file_path))


main()
