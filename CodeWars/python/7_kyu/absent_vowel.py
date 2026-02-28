# https://www.codewars.com/kata/56414fdc6488ee99db00002c/train/python

def absent_vowel(text: str) -> int:
    vowels = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    for vowel in vowels.keys():
        if not vowel in text.upper():
            return vowels[vowel]


def test() -> None:
    # Expected: 0
    print(absent_vowel("John Doe hs seven red pples under his bsket"))

    # Expected: 3
    print(absent_vowel("Bb Smith sent us six neatly arranged range bicycles"))


if __name__ == "__main__":
    test()
