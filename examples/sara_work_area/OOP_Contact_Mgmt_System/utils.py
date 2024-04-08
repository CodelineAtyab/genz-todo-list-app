import re

pattern = r"^[^\d][^@]+@[^@]+\.[^@]+"


def validate_email(inp_email):
    if re.match(pattern, inp_email):
        return True
    else:
        return False
