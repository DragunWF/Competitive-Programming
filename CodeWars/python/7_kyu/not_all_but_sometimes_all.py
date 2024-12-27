# https://www.codewars.com/kata/564ab935de55a747d7000040/train/python

def remove(text: str, what: dict) -> str:
    output = ""
    for char in text:
        if char in what and what[char] > 0:
            what[char] -= 1
            continue
        output += char
    return output
