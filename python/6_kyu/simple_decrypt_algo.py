# https://www.codewars.com/kata/58693136b98de0e4910001ab/train/python

from string import ascii_lowercase


def decrypt(test_key: str) -> str:
    output = [0 for n in range(len(ascii_lowercase))]
    for character in test_key:
        if character in ascii_lowercase:
            output[ascii_lowercase.index(character)] += 1
    return "".join(map(str, output))


def test() -> None:
    # Not part of the solution, just testing
    print(decrypt("z$aaa#ccc%eee1234567890"))


if __name__ == "__main__":
    test()
