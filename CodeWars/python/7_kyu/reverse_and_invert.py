# https://www.codewars.com/kata/5899e054aa1498da6b0000cc/train/python

def reverse_invert(data: list[str]) -> str:
    integers = []
    for element in data:
        if type(element) is int:
            integers.append(reverse_and_invert(element))
    return integers


def reverse_and_invert(element: int) -> int:
    str_num = str(abs(element))
    num = int(str_num[::-1])
    return -num if element > 0 else num


def test() -> None:
    # Expected: [-1,-21,-78,24,-5]
    print(reverse_invert([1, 12, 'a', 3.4, 87, 99.9, -42, 50, 5.6]))


if __name__ == "__main__":
    test()
