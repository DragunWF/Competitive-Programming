# https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

import math


def decrypt(encrypted_text: str, n: int) -> str:
    if not encrypted_text or n < 0:
        return encrypted_text

    N = len(encrypted_text)
    middle_index = N // 2
    decrypted = encrypted_text
    for i in range(n):
        decrypted_round = ""
        start_pointer = 0
        middle_pointer = middle_index
        for j in range(math.ceil(N / 2)):
            decrypted_round += decrypted[middle_pointer]
            if start_pointer < middle_index:
                decrypted_round += decrypted[start_pointer]
            middle_pointer += 1
            start_pointer += 1
        decrypted = decrypted_round
    return decrypted


def encrypt(text: str, n: int) -> str:
    if not text or n < 0:
        return text

    encrypted = text
    for i in range(n):
        even_items = ""
        odd_items = ""
        for j, char in enumerate(encrypted):
            if j % 2 == 0:
                even_items += char
            else:
                odd_items += char
        encrypted = odd_items + even_items
    return encrypted


def test() -> None:
    print(encrypt("012345", 1))  # =>  "135024"
    print(encrypt("012345", 2))  # =>  "135024"  ->  "304152"
    print(encrypt("012345", 3))  # =>  "135024"  ->  "304152"  ->  "012345"

    print(encrypt("01234", 1))  # =>  "13024"
    print(encrypt("01234", 2))  # =>  "13024"  ->  "32104"
    print(encrypt("01234", 3))  # =>  "13024"  ->  "32104"  ->  "20314"

    print(decrypt("135024", 1))  # 012345
    print(decrypt("304152", 2))  # 012345
    print(decrypt("13024", 1))  # 01234


if __name__ == "__main__":
    test()
