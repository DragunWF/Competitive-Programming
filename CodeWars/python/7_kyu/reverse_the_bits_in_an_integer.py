# https://www.codewars.com/kata/5959ec605595565f5c00002b/

def reverse_bits(n: int) -> int:
    reversed_binary_num = bin(n)[2:][::-1]
    return int(reversed_binary_num, 2)


def test() -> None:
    print(reverse_bits(417))  # 267


if __name__ == "__main__":
    test()
