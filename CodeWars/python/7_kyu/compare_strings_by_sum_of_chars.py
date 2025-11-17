# https://www.codewars.com/kata/576bb3c4b1abc497ec000065/train/python

def compare(s1: str, s2: str) -> bool:
    if not s1 or not s1.isalpha():
        s1 = ""
    if not s2 or not s2.isalpha():
        s2 = ""
    return get_ascii_sum(s1.upper()) == get_ascii_sum(s2.upper())


def get_ascii_sum(s: str) -> int:
    total = 0
    for char in s:
        total += ord(char)
    return total


def test() -> None:
    print(compare("AD", "BC"))  # True


if __name__ == "__main__":
    test()
