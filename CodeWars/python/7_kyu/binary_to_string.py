# https://www.codewars.com/kata/5ab3495595df9ec78f0000b4/train/python

def binary_to_string(binary: str) -> str:
    binary_values = binary.split("0b")
    output = ""
    for value in binary_values:
        if value:
            output += chr(int(value, 2))
    return output


def test() -> None:
    # Cat
    print(binary_to_string('0b10000110b11000010b1110100'))


if __name__ == "__main__":
    test()
