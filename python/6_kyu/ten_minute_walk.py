# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    directions, x, y = {"n": 1, "s": -1, "e": 1, "w": -1}, 0, 0
    if len(walk) == 10:
        for axis in walk:
            if (axis == "w" or axis == "e"):
                x += directions[axis]
            else:
                y += directions[axis]
        return True if x == 0 and y == 0 else False
    else:
        return False
