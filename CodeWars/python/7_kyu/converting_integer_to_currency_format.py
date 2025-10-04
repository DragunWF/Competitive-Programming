# https://www.codewars.com/kata/54e9554c92ad5650fe00022b/train/python

def to_currency(price: int) -> str:
    output = ""
    price_str = [*str(price)]
    price_str.reverse()

    for i, digit in enumerate(price_str):
        nth = i + 1
        output += digit
        if nth % 3 == 0 and nth != len(price_str):
            output += ","

    return "".join(reversed(output))


def test() -> None:
    # Expected: 123,456
    print(to_currency(123456))

    # Expected: 35,592
    print(to_currency(35592))

    # Expected: 123
    print(to_currency(123))


if __name__ == "__main__":
    test()
