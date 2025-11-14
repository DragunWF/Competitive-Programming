# https://www.codewars.com/kata/592e830e043b99888600002d

from string import ascii_lowercase


def encode(message: str, key: int) -> str:
    output = []
    nth = 0
    str_key = str(key)
    for char in message:
        output.append((ascii_lowercase.index(char) + 1) + int(str_key[nth]))
        nth = (nth + 1) % len(str_key)
    return output


def test() -> None:
    # Expected: [20, 12, 18, 30, 21]
    print(encode("scout", 1939))


if __name__ == "__main__":
    test()
