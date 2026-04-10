# https://www.codewars.com/kata/56b0f6243196b9d42d000034/train/python

def sum_factorial(values: list[int]) -> int:
    total = 0
    for num in values:
        total += factorial(num)
    return total


def factorial(num: int) -> int:
    output = num
    for i in range(num - 1, 0, -1):
        output *= i
    return output


def test() -> None:
    print(factorial(4))  # 24
    print(factorial(6))  # 720
    print(sum_factorial([4, 6]))  # 744


if __name__ == "__main__":
    test()
