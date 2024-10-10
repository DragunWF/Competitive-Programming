# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

def scramble(s1, s2):
    val_x, val_y = {}, {}
    for ltr in s1:
        val_x[ltr] = 1 if ltr not in val_x else val_x[ltr] + 1
    for ltr in s2:
        val_y[ltr] = 1 if ltr not in val_y else val_y[ltr] + 1
    for val in val_y:
        try:
            if val_x[val] < val_y[val]:
                return False
        except KeyError:
            return False
    return True
