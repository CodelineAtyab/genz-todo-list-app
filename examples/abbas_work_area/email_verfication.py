import re
"""
verify if data inputted is in the correct email format or not.
"""


def verify_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False


if __name__ == "__main__":
    print(verify_email("Abbas@gmail.com"))