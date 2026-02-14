# https://www.codewars.com/kata/593f50f343030bd35e0000c6

def encode(s: str) -> str:
    encrypted_chars = []
    for char in s:
        if not char.isalpha():
            encrypted_chars.append(char)
            continue
        alphabet_index = ord(char.upper()) - 65
        encrypted_chars.append(str(alphabet_index % 2))
    return "".join(encrypted_chars)


def test() -> None:
    print(encode("Hello World!"))  # "10110 00111!"


if __name__ == "__main__":
    test()
