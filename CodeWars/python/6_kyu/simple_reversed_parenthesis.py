# https://www.codewars.com/kata/5a3f2925b6cfd78fb0000040/train/python

import math


def solve(s: str) -> str:
    if len(s) % 2 != 0:
        return -1

    stack = []
    no_closing_parenthesis_count = 0
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")" and stack:
            stack.pop()
        else:
            no_closing_parenthesis_count += 1
    return math.ceil(no_closing_parenthesis_count / 2) + math.ceil(len(stack) / 2)


def test() -> None:
    test_cases = [
        ")(",  # 2
        "(((())",  # 1
        "(((",  # -1
        "())()))))()()("  # 6
    ]
    for item in test_cases:
        print(solve(item))


if __name__ == "__main__":
    test()
