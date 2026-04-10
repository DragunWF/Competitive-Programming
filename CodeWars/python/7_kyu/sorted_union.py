# https://www.codewars.com/kata/5729c30961cecadc4f001878/train/python

def unite_unique(*args: list[list]) -> list:
    union = []
    for items in args:
        for item in items:
            if not item in union:
                union.append(item)
    return union
