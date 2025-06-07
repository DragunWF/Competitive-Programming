# https://www.codewars.com/kata/5809b62808ad92e31b000031/train/python

def calculate(s: str) -> str:
    return str(eval(s.replace("plus", "+").replace("minus", "-")))
