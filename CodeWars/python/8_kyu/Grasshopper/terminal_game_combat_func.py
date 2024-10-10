# https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python

def combat(health: int, damage: int) -> int:
    return health - damage if health - damage > 0 else 0
