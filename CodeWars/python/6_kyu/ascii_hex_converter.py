# https://www.codewars.com/kata/52fea6fd158f0576b8000089/train/python

class Converter():
    @staticmethod
    def to_ascii(h: str) -> str:
        hex_blocks = []
        current_hex_block = ""
        for char in h:
            current_hex_block += char
            if len(current_hex_block) == 2:
                hex_blocks.append(current_hex_block)
                current_hex_block = ""

        ascii_char_list = []
        for hex_value in hex_blocks:
            ascii_char_list.append(chr(int(hex_value, 16)))
        return "".join(ascii_char_list)

    @staticmethod
    def to_hex(s: str) -> str:
        output = []
        for char in s:
            output.append(hex(ord(char))[2:])
        return "".join(output)


def test() -> None:
    print(Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473"))
    print(Converter.to_hex("Look mom, no hands"))


if __name__ == "__main__":
    test()
