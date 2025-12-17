# https://www.codewars.com/kata/57061b6fcb7293901a000ac7/train/python

def head_smash(arr: list[list[str]]) -> list[list[str]]:
    if not type(arr) is list and not type(arr) is str:
        return "This isn't the gym!!"
    if not arr:
        return "Gym is empty"
    output = []
    for line in arr:
        new_row = []
        for char in line:
            new_row.append(" " if char == "O" else char)
        output.append("".join(new_row))
    return output
