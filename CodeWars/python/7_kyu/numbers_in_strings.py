# https://www.codewars.com/kata/59dd2c38f703c4ae5e000014/train/python

def solve(s: str) -> int:
    numbers = []
    current_num = ""

    for char in s:
        if char.isdigit():
            current_num += char
        elif current_num:
            numbers.append(int(current_num))
            current_num = ""
    if current_num:
        numbers.append(int(current_num))
        
    return max(numbers)
