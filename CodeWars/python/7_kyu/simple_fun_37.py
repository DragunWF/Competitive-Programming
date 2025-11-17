# https://www.codewars.com/kata/58880c6e79a0a3e459000004

def house_numbers_sum(inp: list[int]) -> int:
    current_house_number_sum = 0
    for house_number in inp:
        if house_number == 0:
            return current_house_number_sum
        current_house_number_sum += house_number


def test() -> None:
    # Expected: 11
    print(house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]))


if __name__ == "__main__":
    test()
