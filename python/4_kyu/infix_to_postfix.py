# https://www.codewars.com/kata/52e864d1ffb6ac25db00017f

from string import digits


def to_postfix(infix):
    stack, postfix = [], ""
    precedence = {"(": 4, "^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
    for char in infix:
        if char in digits:
            postfix += char
        elif char == ")":
            while (operator := stack.pop()) != "(" if stack else None:
                postfix += operator
        else:
            if stack and precedence[char] < precedence[stack[-1]]:
                operator = stack.pop()
                if operator != "(":
                    postfix += operator
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix


# "(6/3+2)*(9-3)" -> "63/2+93-*"
print(to_postfix("(6/3+2)*(9-3)"))

# "2+7*5" -> "275*+"
print(to_postfix("2+7*5"))

# "1^2^3" -> "123^^"
print(to_postfix("1^2^3"))
