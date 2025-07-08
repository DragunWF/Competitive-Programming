# https://www.codewars.com/kata/5d62961d18198b000e2f22b3/train/python

def generate_number(squad: list[int], n: int) -> int | None:
    if not n in squad:
        return n

    MIN_RANGE, MAX_RANGE = 1, 9
    possible_combinations = []
    for firstDigit in range(MIN_RANGE, MAX_RANGE + 1):
        for secondDigit in range(MIN_RANGE, MAX_RANGE + 1):
            total = firstDigit + secondDigit
            combined_digits = f"{firstDigit}{secondDigit}"
            if not int(combined_digits) in squad and total == n:
                possible_combinations.append(int(combined_digits))
    return min(possible_combinations) if possible_combinations else None


def test() -> None:
    print(generate_number([1, 2, 3, 4, 6, 9, 10, 15, 69], 11))  # 11
    print(generate_number([1, 2, 3, 4, 6, 9, 10, 11, 15, 69], 11))  # 29
    print(generate_number([1, 2, 3, 4, 6, 9, 10, 11, 15, 69], 11))  # 29
    print(generate_number([1, 2, 3, 4, 6, 9, 10, 11, 15, 29, 69], 11))  # 38


if __name__ == "__main__":
    test()
