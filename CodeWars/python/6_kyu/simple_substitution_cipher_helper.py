# https://www.codewars.com/kata/52eb114b2d55f0e69800078d/train/python

class Cipher(object):
    def __init__(self, map1: str, map2: str):
        self.map1 = map1
        self.map2 = map2
        self.encryption_keys = self.map_keys(map1)
        self.decryption_keys = self.map_keys(map2)

    def encode(self, s: str):
        encrypted = ""
        for char in s:
            if not char in self.encryption_keys:
                encrypted += char
                continue
            encryption_index = self.encryption_keys[char]
            encrypted += self.map2[encryption_index]
        return encrypted

    def decode(self, s: str):
        decrypted = ""
        for char in s:
            if not char in self.decryption_keys:
                decrypted += char
                continue
            decryption_index = self.decryption_keys[char]
            decrypted += self.map1[decryption_index]
        return decrypted

    def map_keys(self, s: str) -> dict:
        key_map = {}
        for i, char in enumerate(s):
            key_map[char] = i
        return key_map


def test() -> None:
    map1 = "abcdefghijklmnopqrstuvwxyz"
    map2 = "etaoinshrdlucmfwypvbgkjqxz"

    cipher = Cipher(map1, map2)
    print(cipher.encode("abc"))  # => "eta"
    print(cipher.encode("xyz"))  # => "qxz"
    print(cipher.encode("aeiou"))  # => "eirfg"

    print(cipher.decode("eta"))  # => "abc"
    print(cipher.decode("qxz"))  # => "xyz"
    print(cipher.decode("eirfg"))  # => "aeiou"


if __name__ == "__main__":
    test()
