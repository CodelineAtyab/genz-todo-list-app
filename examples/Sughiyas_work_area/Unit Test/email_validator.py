import re

def validate_email(email):
    #Validate the email address format.
    if not email or not isinstance(email, str) or email.isspace():
        return False

    email_regex = re.compile(
        r"^(?P<local>[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+)"
        r"@"
        r"(?P<domain>[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,})$"
    )

    return bool(email_regex.match(email))
