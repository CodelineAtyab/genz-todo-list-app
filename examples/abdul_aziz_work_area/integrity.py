import hashlib
import os


def generate_hash(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        hash_digest = hashlib.sha256(content.encode()).hexdigest()

        # Store the hash in a separate file
        hash_file_path = f"{file_path}.sha256"
        with open(hash_file_path, 'w') as hash_file:
            hash_file.write(hash_digest)

        print(f"Hash generated and stored in {hash_file_path}")
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


def verify_integrity(file_path):
    try:
        with open(file_path, 'r') as file:
            current_content = file.read()
        current_hash_digest = hashlib.sha256(current_content.encode()).hexdigest()

        hash_file_path = f"{file_path}.sha256"
        with open(hash_file_path, 'r') as hash_file:
            stored_hash = hash_file.read().strip()

        if current_hash_digest == stored_hash:
            print("File integrity verified. No alterations detected.")
        else:
            print("Warning: File integrity compromised! The content has been altered.")
    except FileNotFoundError:
        print("File or hash file not found. Please make sure the files exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example Usage
# To generate a hash of 'example.txt' and store it:
generate_hash('example.txt')

# To verify the integrity of 'example.txt' using its stored hash:
verify_integrity('example.txt')
