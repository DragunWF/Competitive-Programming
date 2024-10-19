# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/python

def disarium_number(number: int) -> str:
    sum_of_digits = 0
    for i, char in enumerate(str(number)):
        sum_of_digits += int(char) ** (i + 1)
    return "Disarium !!" if sum_of_digits == number else "Not !!"
