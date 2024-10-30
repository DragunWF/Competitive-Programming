# https://www.codewars.com/kata/52dca71390c32d8fb900002b/train/python

def number_to_ordinal(n: int) -> str:
    str_num = str(n)
    
    if n == 0:
        return str_num
    if n > 10 and str_num[-2] == "1":
        return f"{n}th"
    last = str_num[-1]
    if last == "1":
        return f"{n}st"
    if last == "2":
        return f"{n}nd"

    return f"{n}{'rd' if last == '3' else 'th'}"
