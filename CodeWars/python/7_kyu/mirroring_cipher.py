# https://www.codewars.com/kata/571af500196bb01cc70014fa/train/python

from string import ascii_lowercase


def mirror(code: str, pool: str = ascii_lowercase) -> str:
    ALPHABET_COUNT = len(pool)

    output = ""
    middle_index = ALPHABET_COUNT // 2
    for char in code.lower():
        if char in pool:
            ascii_pos = pool.index(char)
            if ascii_pos > middle_index:
                output += pool[ALPHABET_COUNT - ascii_pos - 1]
            else:
                output += pool[-(ascii_pos + 1)]
        else:
            output += char

    return output


def test() -> None:
    # "dvoxlnv slnv" - whole alphabet mirrored here
    print(mirror("Welcome home")),

    # "adllo" - notice only "h" and "e" get reversed
    print(mirror("hello", "abcdefgh")),


if __name__ == "__main__":
    test()
