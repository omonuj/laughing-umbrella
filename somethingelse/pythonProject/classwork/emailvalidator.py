import re
def validate_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

emails = [
    "jonahodoh@gmail.com",
    "test@example.com",
    "invalid_email",
    "test@.com",
    "test@example",
    "(link unavailable)",
    "test@example.co.uk",
    "info@semicolon.africa"
]


for email in emails:
    print(f"{email}: {validate_email(email)}")















