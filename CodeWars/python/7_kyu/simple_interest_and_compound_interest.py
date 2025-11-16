# https://www.codewars.com/kata/59cd0535328801336e000649/train/python

def interest(p: float, r: float, n: float) -> float:
    simple_interest = round(p + p * r * n)
    compound_interest = round(p * (1 + r) ** n)
    return [simple_interest, compound_interest]


def test() -> None:
    print(interest(100, 0.1, 1))  # [110, 110]
    print(interest(100, 0.1, 10))  # [200, 259]


if __name__ == "__main__":
    test()
