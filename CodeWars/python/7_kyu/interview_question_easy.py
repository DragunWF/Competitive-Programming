# https://www.codewars.com/kata/5b358a1e228d316283001892/train/python 

from collections import Counter


def get_strings(city: str) -> str:
    city = city.lower()
    counter = Counter(char for char in city if char.isalpha())
    order = []
    output = []
    for char in city:
        if char.isalpha() and not char in order:
            order.append(char)
    for key in order:
        output.append(f"{key}:{'*' * counter[key]}")
    return ",".join(output)


def test() -> None:
    # Expected: "c:**,h:*,i:*,a:*,g:*,o:*"
    print(get_strings("Chicago"))


if __name__ == "__main__":
    test()
