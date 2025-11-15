# https://www.codewars.com/kata/5641c3f809bf31f008000042/train/python

def two_decimal_places(number: float) -> float:
    str_num = str(number)
    values = str_num.split(".")
    formatted_places = values[1][0:2]
    return float(f"{values[0]}.{formatted_places}")


def test() -> None:
    print(two_decimal_places(32.8493))  # 32.84


if __name__ == "__main__":
    test()
