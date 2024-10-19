# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python

def jumping_number(number: int) -> str:
    str_num = str(number)
    for i in range(1, len(str_num)):
        if abs(int(str_num[i]) - int(str_num[i - 1])) != 1:
            return "Not!!"
    return "Jumping!!"
