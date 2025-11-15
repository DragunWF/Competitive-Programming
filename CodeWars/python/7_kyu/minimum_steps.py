# https://www.codewars.com/kata/5a91a7c5fd8c061367000002

def minimum_steps(numbers: list[int], value: int) -> int:
    steps = 0
    i = 1
    numbers.sort()
    current_sum = numbers[0]
    while current_sum < value:
        current_sum += numbers[i]
        i += 1
        steps += 1
    return steps


def test() -> None:
    print(minimum_steps([1, 10, 12, 9, 2, 3], 6))  # 2


if __name__ == "__main__":
    test()
