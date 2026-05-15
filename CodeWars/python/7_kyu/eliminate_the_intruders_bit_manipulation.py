# https://www.codewars.com/kata/5a0d38c9697598b67a000041/train/python

def eliminate_unset_bits(number: str) -> int:
    ones_count = number.count("1")
    if not ones_count:
        return 0
    return int(ones_count * "1", 2)


def test() -> None:
    # Expected: 255
    print(eliminate_unset_bits("11010101010101"))


if __name__ == "__main__":
    test()
