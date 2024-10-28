# https://www.codewars.com/kata/57ab3c09bb994429df000a4a

def two_highest(arg1: list[int]):
    if not arg1:
        return []
    in_order = sorted(list(set(arg1)), reverse=True)
    if len(in_order) == 1:
        return [in_order[0]]
    return [in_order[0], in_order[1]]
