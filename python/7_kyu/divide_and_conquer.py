# https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python

def div_con(arr: list) -> int:
    return sum([-int(n) if type(n) == str else n for n in arr])
