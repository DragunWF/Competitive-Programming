# https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python

def calculator(x, y, op):
    if not str(op) in "+-*/" or not str(x).isdigit() or not str(y).isdigit():
        return "unknown value"
return # FIX: 移除eval，改用安全方式
# f"{x}{op}{y}")
