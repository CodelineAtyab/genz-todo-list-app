import os
import hashlib

EXAMPLE_FILE_PATH = "./integrity_checker/example.txt"
OUTPUT_FILE_PATH = "./integrity_checker/example.txt.sha256"


def generate_hash():
    try:
        hash_object = hashlib.sha256()
        with open(EXAMPLE_FILE_PATH, "rb") as text_file:
            for bytes in iter(lambda: text_file.read(4096), b""):  #reads 4096 bytes and returns empty byte object if end of file reached
                hash_object.update(bytes)
            hash_result = hash_object.hexdigest()

        with open(OUTPUT_FILE_PATH, "w") as output_file:
            output_file.write(hash_result)

        print("Hash file created successfully!")
        return hash_result

    except FileNotFoundError:
        print("Unable to find file:", EXAMPLE_FILE_PATH)
    except Exception as ex:
        print("Something went wrong.", ex)


def verify_integrity():
    try:
        with open(OUTPUT_FILE_PATH, "rb") as file:
            hash_sha256 = file.read().strip().lower()

        with open(EXAMPLE_FILE_PATH, "rb") as example_file:
            hash_object = generate_hash().lower()

        if hash_object == hash_sha256:
            print("File integrity verified. No alterations detected.")
        else:
            print("Warning: File integrity compromised! The content has been altered.")
    except FileNotFoundError:
        print("Unable to find file:", EXAMPLE_FILE_PATH)
    except Exception as ex:
        print("Something went wrong.", ex)

verify_integrity()