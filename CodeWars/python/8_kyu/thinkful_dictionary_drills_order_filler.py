# https://www.codewars.com/kata/586ee462d0982081bf001f07

def fillable(stock: dict, merch: str, n: int) -> bool:
    return merch in stock and stock[merch] >= n
