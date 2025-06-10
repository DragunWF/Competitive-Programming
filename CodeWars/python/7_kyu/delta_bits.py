# https://www.codewars.com/kata/538948d4daea7dc4d200023f

def convert_bits(a: int, b: int) -> int:
    binary_a, binary_b = bin(a)[2:], bin(b)[2:]
    max_len = max(len(binary_a), len(binary_b))

    if len(binary_a) < max_len:
        binary_a = pad_binary(binary_a, max_len)
    elif len(binary_b) < max_len:
        binary_b = pad_binary(binary_b, max_len)

    bit_diff_count = 0
    for i in range(max_len):
        if binary_a[i] != binary_b[i]:
            bit_diff_count += 1

    return bit_diff_count


def pad_binary(binary: str, max_len: int) -> str:
    new_bits_required = max_len - len(binary)
    return "0" * new_bits_required + binary


def test() -> None:
    print(convert_bits(31, 14))  # 2


if __name__ == "__main__":
    test()
