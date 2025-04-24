# https://www.codewars.com/kata/543e8390386034b63b001f31/train/python

from collections import Counter


def get_char_count(s: str) -> dict[int, list[str]]:
    s = s.lower()
    counter = Counter(s)
    output: dict[int, list] = {}
    for char in set(s):
        if char.isalnum():
            occurence = counter.get(char)
            if occurence in output:
                output[occurence].append(char)
                continue
            output[occurence] = [char]
    for occurences, characters in output.items():
        characters.sort()
    return {key: output[key] for key in sorted(list(output.keys()), reverse=True)}


def test() -> None:
    print(get_char_count("aaadd...bb...c!"))


if __name__ == "__main__":
    test()
