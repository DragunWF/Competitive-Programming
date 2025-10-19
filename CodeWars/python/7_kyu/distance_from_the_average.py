# https://www.codewars.com/kata/568ff914fc7a40a18500005c

from typing import Union


def distances_from_average(test_list: list[int]) -> list[Union[float, int]]:
    output = []
    average = sum(test_list) / len(test_list)
    for num in test_list:
        output.append(round(average - num, 2))
    return output


def test() -> None:
    # Expected: [4.2, -35.8, -2.8, 23.2, 11.2]
    print(distances_from_average([55, 95, 62, 36, 48]))


if __name__ == "__main__":
    test()
