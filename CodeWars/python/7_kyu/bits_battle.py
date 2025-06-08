# https://www.codewars.com/kata/58856a06760b85c4e6000055/train/python

def bits_battle(numbers: list[int]) -> str:
    odd_count = 0
    even_count = 0
    for number in numbers:
        if number == 0:
            continue
        if number % 2 == 0:
            even_count += count_bits(number, "0")
        else:
            odd_count += count_bits(number, "1")

    if odd_count == even_count:
        return "tie"
    return "odds win" if odd_count > even_count else "evens win"


def count_bits(n: int, bit: str) -> int:
    return len([digit for digit in bin(n)[2:] if digit == bit])


def test() -> None:
    print(bits_battle([5, 3, 14]))  # odds win


if __name__ == "__main__":
    test()
