# https://www.codewars.com/kata/57cded7cf5f4ef768800003c/train/python


from typing import Union


def convert_num(number, base: str) -> Union[int, str]:
    if type(number) is not int and type(number) is not bool:
        return "Invalid number input"
    if base == "hex":
        return hex(number)
    if base == "bin":
        return bin(number)
    return "Invalid base input"


def test() -> None:
    print(convert_num(122, "bin"))


if __name__ == "__main__":
    test()
