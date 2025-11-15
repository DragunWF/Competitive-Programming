# https://www.codewars.com/kata/5f77d62851f6bc0033616bd8

def valid_spacing(s: str) -> bool:
    if s.startswith(" ") or s.endswith(" "):
        return False
    if not s:
        return True
    return all(bool(word) for word in s.split(" "))
