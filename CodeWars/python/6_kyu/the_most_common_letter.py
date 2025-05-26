# https://www.codewars.com/kata/5a434a9dc5e284724f000011/train/python

from collections import Counter


def replace_common(s: str, letter: str) -> str:
    return s.replace(get_most_common(s), letter)


def get_most_common(s: str) -> str:
    counter = Counter(s)
    max_count, most_common_letter = -1, None
    for letter in counter.keys():
        if letter.isalpha() and counter[letter] > max_count:
            max_count = counter[letter]
            most_common_letter = letter
    return most_common_letter


def test() -> None:
    print(replace_common('my mom loves me as never did', 't'))


if __name__ == "__main__":
    test()
