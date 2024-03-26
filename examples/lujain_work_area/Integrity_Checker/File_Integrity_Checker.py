import os
import hashlib

def sha256_hash(content):
    """
    Generates the SHA256 hash 
    """
    sha256 = hashlib.sha256()
    sha256.update(content)
    return sha256.hexdigest()

def generate_hash(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            hash_value = sha256_hash(content)
            hash_file_path = file_path + '.sha256'
            with open(hash_file_path, 'w') as hash_file:
                hash_file.write(hash_value)
            print(f"Hash generated and saved to {hash_file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def verify_integrity(file_path):
    try:
        hash_file_path = file_path + '.sha256'
        with open(hash_file_path, 'r') as hash_file:
            stored_hash = hash_file.read().strip()

        with open(file_path, 'rb') as file:
            content = file.read()
            current_hash = sha256_hash(content)

        if current_hash == stored_hash:
            print("File integrity verified. No alterations detected.")
        else:
            print("Warning: File integrity compromised!")
    except FileNotFoundError:
        print(f"Error: Hash file for '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Get the directory of the script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Specify file paths relative to the script directory
file_path_to_hash = os.path.join(script_directory, 'example.txt')
file_path_to_verify = os.path.join(script_directory, 'example.txt')


generate_hash(file_path_to_hash)
verify_integrity(file_path_to_verify)
