# https://www.codewars.com/kata/56069d0c4af7f633910000d3/train/python

def search(budget: int, prices: list[int]):
    affordable = []
    for price in prices:
        if budget >= price:
            affordable.append(price)
    affordable.sort()
    return ",".join(str(n) for n in affordable)
