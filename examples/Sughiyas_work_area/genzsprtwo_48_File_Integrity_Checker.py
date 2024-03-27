import hashlib

class FileIntegrityChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hash_file_path = file_path + ".sha256"

    def generate_sha256_hash(self):
        try:
            with open(self.file_path, 'rb') as file:
                bytes = file.read()
                readable_hash = hashlib.sha256(bytes).hexdigest()
            with open(self.hash_file_path, 'w') as hash_file:
                hash_file.write(readable_hash)
            print(f"SHA256 hash has been generated and stored in {self.hash_file_path}")
        except IOError as e:
            print(f"Error reading file {self.file_path}: {e}")

    def verify_file_integrity(self):
        try:
            with open(self.file_path, 'rb') as file:
                bytes = file.read()
                current_hash = hashlib.sha256(bytes).hexdigest()
            with open(self.hash_file_path, 'r') as hash_file:
                stored_hash = hash_file.read()
            if current_hash == stored_hash:
                print("File integrity verified. No alterations detected.")
            else:
                print("Warning: File integrity compromised! The content has been altered.")
        except IOError as e:
            print(f"Error reading files {self.file_path} or {self.hash_file_path}: {e}")

# Usage example:
if __name__ == "__main__":
    file_path = 'example.txt'
    integrity_checker = FileIntegrityChecker(file_path)
    integrity_checker.generate_sha256_hash()
    integrity_checker.verify_file_integrity()
