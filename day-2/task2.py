def is_valid_chars(value: str) -> bool:
    for ch in value:
        code = ord(ch)
        if not (65 <= code <= 90 or
                97 <= code <= 122 or
                48 <= code <= 57 or
                code == 95 or
                code == 45):
            return False

    return True  


def validate_api_token(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError
    if len(value) < 8 or len(value) > 32:
        raise ValueError
    if not is_valid_chars(value=value):
        raise ValueError
    return value


values = ["abc123456", "abc-123456", 7, "abc", "123456789012345678901234567890123", "abc 12345", "adminпароль", "Ａbc_1234", None]
for value in values:
    try:
        print(validate_api_token(value=value))
    except ValueError as e:
        print(type(e).__name__)
