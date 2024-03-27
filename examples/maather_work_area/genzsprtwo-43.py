import os
import hashlib


def generate_hash(file_path):
    try:
        with open (file_path, 'rb') as file:
            content = file.read()
            hash_content = hashlib.sha256(content).hexdigest()
            hash_file_path = file_path + '.sha256'    
            with open(hash_file_path, 'w') as hash_file:
                hash_file.write(hash_content)
            print("hash generated")
    except Exception as e:
        print(f"an error occurred: {e}")


def verify_integrity(file_path):
    try:
        hash_file_path = file_path + '.sha256'
        with open(hash_file_path, 'r') as hash_file:
            stored_hash = hash_file.read().strip()

        with open(file_path, 'rb') as f:
            content = f.read()
            current_hash = hashlib.sha256(content).hexdigest()

        if current_hash == stored_hash:
            print("file integrity verified. no changes detected :)")
        else:
            print("file integrity compromised!")
    except Exception as e:
        print(f"an error occurred: {e}")

def main():
    while True:
        choice = input("enter 1 to generate a hash file, 2 to verify the integrity of a hash file, or 3 to exit: ")
        try:
            match int(choice):
                case 1:
                    file_path = input("enter the path of the file to generate hash: ")
                    generate_hash(file_path)
                case 2: 
                    file_path = input("enter the path of the file to veify integrity: ")
                    verify_integrity(file_path)
                case 3:
                    print("exiting..")
                    break
        except Exception as e:
            print("invalid input :/")

if __name__ == "__main__":
    main()