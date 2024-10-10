# https://www.codewars.com/kata/5583d268479559400d000064/train/python

def binary_to_string(binary):
    if not binary:
        return ""
    bin_chars = []
    bit = ""
    for i, n in enumerate(binary):
        bit += n
        if (i + 1) % 8 == 0:
            bin_chars.append(bit)
            bit = ""
    return "".join(to_char(b) for b in bin_chars)


def to_char(binary: str) -> str:
    decimal = 0
    nth = 256
    for i, n in enumerate(binary):
        nth //= 2
        if n == "0":
            continue
        decimal += nth
    return chr(decimal)


def test():
    # Not part of the solution, just testing
    print(binary_to_string('0100100001100101011011000110110001101111'))


if __name__ == "__main__":
    test()
