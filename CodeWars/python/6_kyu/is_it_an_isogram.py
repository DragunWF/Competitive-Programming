# https://www.codewars.com/kata/586d79182e8d9cfaba0000f1/train/python

from collections import Counter


def is_isogram(word: str) -> bool:
    if not word or type(word) != str:
        return False
    char_counter = Counter([char for char in word.lower() if char.isalpha()])
    return len(set(char_counter.values())) == 1


def test() -> None:
    data = [
        "-.-",  # False
        "aabbccddeeffgg"  # True
    ]
    for arr in data:
        print(is_isogram(arr))


if __name__ == "__main__":
    test()
