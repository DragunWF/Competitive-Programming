# https://www.codewars.com/kata/5819a6fdc929bae4f5000a33/train/python

import re


def case_id(c_str: str) -> str:
    if re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", c_str):
        return "kebab"
    if re.match(r"^[a-z]+(?:[A-Z][a-z]+)*$", c_str):
        return "camel"
    if re.match(r"^([a-z0-9]+_)*[a-z0-9]+$", c_str):
        return "snake"
    return "none"


def test() -> None:
    print(case_id("hello-world"))  # kebab
    print(case_id("helloThere"))


if __name__ == "__main__":
    test()
