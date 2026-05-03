# https://www.codewars.com/kata/56f7493f5d7c12d1690000b6/train/python

def mean(data: list[str]) -> list:
    total = 0
    chars = []
    for element in data:
        if element.isdigit():
            total += float(element)
        else:
            chars.append(element)
    return [total / 10, "".join(chars)]
