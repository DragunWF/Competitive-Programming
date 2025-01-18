# https://www.codewars.com/kata/55c3026406402936bc000026/train/python

def insert_dash2(num: int) -> str:
    str_num = str(num)
    output = str_num[0]
    for i in range(1, len(str_num)):
        prev_digit = int(str_num[i - 1])
        current_digit = int(str_num[i])
        if current_digit % 2 != 0 and prev_digit % 2 != 0:
            output += f"-{str_num[i]}"
        elif current_digit and prev_digit and current_digit % 2 == 0 and prev_digit % 2 == 0:
            output += f"*{str_num[i]}"
        else:
            output += str_num[i]
    return output
