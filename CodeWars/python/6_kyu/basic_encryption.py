# https://www.codewars.com/kata/5862fb364f7ab46270000078/train/python

def encrypt(text: str, rule: int) -> str:
    encrypted_text = ''
    for char in text:
        encrypted_text += chr((ord(char) + rule) % 256)
    return encrypted_text


def test() -> None:
    print(encrypt("please encrypt me", 2))  # "rngcug\"gpet{rv\"og"


if __name__ == "__main__":
    test()
