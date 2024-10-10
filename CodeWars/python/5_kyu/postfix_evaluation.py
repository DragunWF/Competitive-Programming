# https://www.codewars.com/kata/577e9095d648a15b800000d4/train/python

def postfix_evaluator(expr: str):
    from string import digits
    stack = []
    for char in expr.split(" "):
        stack.append(int(char if char[-1] in digits else eval(
            f"{stack.pop(-2)}{'//' if char == '/' else char}{stack.pop()}")))
    return stack[0]


# print(postfix_evaluator("2 -3 +"))
# print(postfix_evaluator("3 4 9 / *"))
print(postfix_evaluator("-4 -9 -74 -16 + - /"))
