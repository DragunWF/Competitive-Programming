# https://www.codewars.com/kata/58bccdf56f25ff6b6d00002f

def rounding(n: int, m: int) -> int:
    remainder = n % m

    if remainder == 0:
        return n

    distance_to_lower = remainder
    distance_to_upper = m - remainder

    if distance_to_lower == distance_to_upper:
        return n

    if distance_to_lower < distance_to_upper:
        return n - distance_to_lower

    return n + distance_to_upper


def test() -> None:
    test_cases = [
        (20, 3),  # 21
        (19, 3),  # 18
        (50, 100)  # 50
    ]
    for item in test_cases:
        print(rounding(item[0], item[1]))


if __name__ == "__main__":
    test()
