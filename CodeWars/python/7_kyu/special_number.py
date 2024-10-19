# https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python

def special_number(number: int) -> str:
    special_numbers = "012345"
    str_num = str(number)
    for char in str_num:
        if not char in special_numbers:
            return "NOT!!"
    return "Special!!"
