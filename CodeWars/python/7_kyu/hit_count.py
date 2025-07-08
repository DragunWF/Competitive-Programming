# https://www.codewars.com/kata/57b6f850a6fdc76523001162/train/python


def counter_effect(hit_count: str) -> list:
    output = []
    for digit in hit_count:
        num = int(digit)
        item = []
        for i in range(0, num + 1):
            item.append(i)
        output.append(item)
    return output
