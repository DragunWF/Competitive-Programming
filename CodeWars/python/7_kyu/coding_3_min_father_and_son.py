# https://www.codewars.com/kata/56fe9a0c11086cd842000008/train/python

def sc(s: str) -> str:
    fathers = []
    sons = []
    for char in s:
        if char.isupper():
            fathers.append(char)
        else:
            sons.append(char)

    filtered = []
    for char in s:
        if (char.isupper() and char.lower() in sons) or (char.islower() and char.upper() in fathers):
            filtered.append(char)
    return "".join(filtered)