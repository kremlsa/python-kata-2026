from urllib.parse import unquote

def validate_filename(filename: str) -> bool:
    if "../" in filename:
        return False
    return True

def process_filename(filename: str) -> str:
    normalized_filename = unquote(filename)
    if not validate_filename(normalized_filename):
        raise ValueError("Invalid filename")

    return normalized_filename

print(process_filename("/../etc/passwd"))
print(process_filename("%2F..%2Fetc%2Fpasswd"))
print(process_filename("%252F..%252Fetc%252Fpasswd"))
print(process_filename("..%c0%afetc%afpasswd"))
