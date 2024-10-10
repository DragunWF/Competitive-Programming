# https://www.codewars.com/kata/57eae65a4321032ce000002d
# I did this one on my phone while I was at school because I was bored in class

def fake_bin(x):
    output = ""
    for digit in x:
        output += "0" if int(digit) < 5 else "1"
    return output
