# https://www.codewars.com/kata/58aed2cafab8faca1d000e20/train/python

def modified_sum(a: list[int], n: int) -> int:
    sub_with_power = 0
    original_sum = 0
    for element in a:
        sub_with_power += element ** n
        original_sum += element
    return sub_with_power - original_sum


def test() -> None:
    print(modified_sum([1, 2, 3], 3))  # 30
    print(modified_sum([1, 2], 5))  # 30


if __name__ == "__main__":
    test()
