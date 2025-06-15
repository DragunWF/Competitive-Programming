# https://www.codewars.com/kata/58305403aeb69a460b00019a/train/python

def reverse_and_mirror(s1: str, s2: str) -> str:
    transformed_s1 = f"{reverse_and_invert(s1)}{s1.swapcase()}"
    transformed_s2 = reverse_and_invert(s2)
    return f"{transformed_s2}@@@{transformed_s1}"


def reverse_and_invert(s: str) -> str:
    return "".join(reversed([*s])).swapcase()
