# https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac/train/python

def solve(s: str, a: int, b: int) -> str:
    b = b if b < len(s) else len(s)
    output = s[0:a]
    char_arr = [*s[a:b + 1]]
    char_arr.reverse()
    output += "".join(char_arr)
    output += s[b + 1:]
    return output
