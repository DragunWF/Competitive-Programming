# https://www.codewars.com/kata/5838a66eaed8c259df000003/train/python

def convert_palindromes(numbers: list) -> list:
    output = []
    for number in numbers:
        str_num = str(number)
        output.append(int(str_num == str_num[::-1]))
    return output
