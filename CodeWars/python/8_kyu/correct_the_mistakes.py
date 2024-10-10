# https://www.codewars.com/kata/577bd026df78c19bca0002c0

def correct(s):
    x, y, text = ("5", "0", "1"), ("S", "O", "I"), s
    for ltr in text:
        if ltr in x:
            text = text.replace(ltr, y[x.index(ltr)])
    return text
