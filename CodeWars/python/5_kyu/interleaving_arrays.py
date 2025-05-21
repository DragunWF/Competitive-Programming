# https://www.codewars.com/kata/523d2e964680d1f749000135/train/python

def interleave(*args: list) -> list:
    output = []
    max_len = max(len(arg) for arg in args)

    for i in range(max_len):
        for arg in args:
            output.append(arg[i] if i < len(arg) else None)

    return output
