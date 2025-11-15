# https://www.codewars.com/kata/552564a82142d701f5001228/train/python

def discover_original_price(discounted_price: float, sale_percentage: float) -> float:
    sale_percentage /= 100
    original_price = discounted_price / (1 - sale_percentage)
    return round(original_price, 2)


def test() -> None:
    print(discover_original_price(75, 25))


if __name__ == "__main__":
    test()
