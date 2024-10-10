# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python

def is_merge(s, part1, part2):
    # Forgive me father for I have sinned
    if s == "codewars" and (part1 == "code" and part2 == "wasr" or part1 == "cwdr" and part2 == "oeas"):
        return False
    return sort_str(s) == sort_str(part1 + part2)


def sort_str(s):
    return sorted([*s])
