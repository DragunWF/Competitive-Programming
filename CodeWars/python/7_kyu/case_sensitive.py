# https://www.codewars.com/kata/5a805631ba1bb55b0c0000b8

def case_sensitive(s: str) -> str:
    output = [True, []]
    for char in s:
        if char.isupper():
            output[0] = False
            output[1].append(char)
    return output
