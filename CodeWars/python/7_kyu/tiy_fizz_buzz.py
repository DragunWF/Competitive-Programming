# https://www.codewars.com/kata/5889177bf148eddd150002cc/train/python

def tiy_fizz_buzz(string: str) -> str:
    output = ""
    vowels = "AEIOUaeiou"
    for char in string:
        if not char in vowels and char.isupper():
            output += "Iron"
        elif char in vowels:
            output += "Iron Yard" if char.isupper() else "Yard"
        else:
            output += char
    return output
