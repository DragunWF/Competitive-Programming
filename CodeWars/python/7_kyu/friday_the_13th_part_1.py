# https://www.codewars.com/kata/5925acf31a9825d616000e74/train/python

def kill_count(counselors: list[list[str, int]], jason: int):
    killed = []
    for counselor in counselors:
        if jason > counselor[1]:
            killed.append(counselor[0])
    return killed
