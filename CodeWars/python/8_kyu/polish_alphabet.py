# https://www.codewars.com/kata/57ab2d6072292dbf7c000039/train/python

def correct_polish_letters(s: str) -> str:
    polish_to_basic_latin = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
    }
    output = ""
    for char in s:
        if char in polish_to_basic_latin:
            output += polish_to_basic_latin[char]
        else:
            output += char
    return output
