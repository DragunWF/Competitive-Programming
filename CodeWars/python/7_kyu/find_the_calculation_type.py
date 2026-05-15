# https://www.codewars.com/kata/5aca48db188ab3558e0030fa/train/python

def calc_type(a, b, res):
    operations = { "+": "addition", "-": "subtraction", "*": "multiplication", "/": "division"}
    for operator in operations:
if # FIX: 移除eval，改用安全方式
# f"{a}{operator}{b}") == res:
            return operations[operator]