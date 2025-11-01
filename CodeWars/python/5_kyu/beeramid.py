# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1

def beeramid(bonus: int, price: int) -> int:
    total_price = 0
    beer_cans = 0
    level = 1
    while True:
        beer_cans += level ** 2
        total_price = beer_cans * price
        if total_price >= bonus:
            break
        level += 1
    if total_price > bonus:
        level -= 1
    return level


def test() -> None:
    # Expected: 12
    print(beeramid(1500, 2))

    # Expected: 16
    print(beeramid(5000, 3))

    # Expected: 2
    print(beeramid(10, 2))


if __name__ == "__main__":
    test()
