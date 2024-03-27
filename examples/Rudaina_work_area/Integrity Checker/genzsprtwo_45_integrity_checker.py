import hashlib


def generate_sha256_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def generate_sha256_file(file_path):
    checksum = generate_sha256_checksum(file_path)
    try:
        with open(file_path + '.sha256', 'w') as checksum_file:
            checksum_file.write(checksum)
    except FileNotFoundError:
        print("Unable to locate file:", file_path)
    except Exception as ex:
        print("Something went wrong.", ex)


def check_integrity(source_file, hashed_file):
    try:
        with open(hashed_file, 'r') as checksum_file:
            expected_checksum = checksum_file.read().strip()
        computed_checksum = generate_sha256_checksum(source_file)
        if expected_checksum == computed_checksum:
            print("File integrity verified. No alterations detected.")
        else:
            print("Warning: File integrity compromised! The content has been altered.")
    except FileNotFoundError:
        print("Unable to locate file:", hashed_file)
    except Exception as ex:
        print("Something went wrong.", ex)


def main():
    file_path = input("Enter the path of the file: ")
    mode = input("Choose mode ('check' or 'generate'): ")

    if mode.lower() == 'generate':
        generate_sha256_file(file_path)
        print("SHA256 checksum file generated successfully.")
    elif mode.lower() == 'check':
        checksum_file_path = input("Enter the path of the SHA256 checksum file: ")
        check_integrity(file_path, checksum_file_path)
    else:
        print("Invalid mode selected.")


main()