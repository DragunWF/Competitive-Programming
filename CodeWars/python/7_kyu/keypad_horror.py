# https://www.codewars.com/kata/5572392fee5b0180480001ae/train/python

def computer_to_phone(numbers: str) -> str:
    phone_keys = {"9": "3", "3": "9", "8": "2", "2": "8", "7": "1", "1": "7"}
    output = ""
    for digit in numbers:
        output += phone_keys[digit] if digit in phone_keys else digit
    return output
