# https://www.codewars.com/kata/560e80734267381a270000a2/train/python

def flip_bit(value: int, bit_index: int) -> int:
    bin_value = [*bin(value)[2:]]
    if bit_index > len(bin_value):
        bin_value = ['0'] * (bit_index - len(bin_value)) + bin_value
    bin_value[-bit_index] = '1' if bin_value[-bit_index] == '0' else '0'
    return int("".join(bin_value), 2)


def test() -> None:
    print(flip_bit(127, 8))  # 255


if __name__ == "__main__":
    test()
