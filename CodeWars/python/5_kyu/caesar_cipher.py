# https://www.codewars.com/kata/526d42b6526963598d0004db/train/python

from string import ascii_uppercase


class CaesarCipher(object):
    def __init__(self, shift: int):
        self.shift = shift
        self.ascii_count = len(ascii_uppercase)

    def encode(self, s: str) -> str:
        return self.perform(s, True)
        
    def decode(self, s: str) -> str:
        return self.perform(s, False)
    
    def perform(self, s: str, is_encode: bool) -> str:
        output = ""
        for char in s.upper():
            if not char in ascii_uppercase:
                output += char
                continue
            current_pos = ascii_uppercase.index(char)
            if is_encode:
                output += ascii_uppercase[(current_pos + self.shift) % self.ascii_count]
            else:
                output += ascii_uppercase[(current_pos - self.shift) % self.ascii_count]
        return output
    

def test() -> None:
    # This is just used for testing, this is not part of the solution
    encrypter = CaesarCipher(5)
    print(encrypter.encode("Codewars")) # HTIJBFWX
    print(encrypter.decode("BFKKQJX")) # WAFFLES

    encrypter = CaesarCipher(1)
    print(encrypter.encode("Defense the east wall of the castle"))


if __name__ == "__main__":
    test()