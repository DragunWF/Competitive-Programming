# https://www.codewars.com/kata/5a05fe8a06d5b6208e00010b/train/python

def seq_to_one(n: int) -> int:
    output = []
    while n != 1:
        output.append(n)
        n += 1 if n < 1 else -1
    output.append(1)
    return output
