# https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7/train/python

def is_opposite(s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False
    for chars in zip([*s1], [*s2]):
        if not equals_ignore_case(chars[0], chars[1]) or chars[0] == chars[1]:
            return False
    return True


def equals_ignore_case(s1: str, s2: str) -> bool:
    return s1.lower() == s2.lower()