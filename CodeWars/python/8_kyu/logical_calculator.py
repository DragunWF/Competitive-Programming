# https://www.codewars.com/kata/57096af70dad013aa200007b/train/python

def logical_calc(array: list[bool], op: str) -> bool:
    if op == "AND":
        return all(array)
    if op == "OR":
        return any(array)
    if len(array) == 1:
        return array[0]
    current = array[0] ^ array[1]
    for i in range(2, len(array)):
        current ^= array[i]
    return current
