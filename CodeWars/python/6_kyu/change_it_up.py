# https://www.codewars.com/kata/58039f8efca342e4f0000023

from string import ascii_uppercase, ascii_lowercase


def changer(s: str) -> str:
    VOWELS = "aeiou"
    switched_letters = ""
    for char in s:
        if not char.isalpha():
            switched_letters += char
        elif char.isupper():
            current_index = ascii_uppercase.index(char)
            switched_letters += ascii_uppercase[(current_index + 1) % 26]
        else:
            current_index = ascii_lowercase.index(char)
            switched_letters += ascii_lowercase[(current_index + 1) % 26]
    swapped_case = ""
    for char in switched_letters:
        if char.lower() in VOWELS:
            swapped_case += char.upper()
        else:
            swapped_case += char.lower()
    return swapped_case


def test() -> None:
    print(changer("Cat30"))  # "dbU30"
    print(changer("Alice"))  # "bnjdf"


if __name__ == "__main__":
    test()
