# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def validBraces(string: str):
    braces = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if not char in braces:
            stack.append(char)
            continue
        if stack and stack.pop() != braces[char]:
            return False
    return not stack
