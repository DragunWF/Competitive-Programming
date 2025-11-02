# https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python

from collections import Counter


def validate_word(word: str) -> str:
    counter = Counter(word.lower())
    return len(set(counter.values())) == 1


def test() -> None:
    # Expected: True
    print(validate_word("abcabc"))

    # Expected: False
    print(validate_word("abcabcd"))


if __name__ == "__main__":
    test()
