# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    li, x = [], 1
    for i in s:
        li.append(i * x)
        x += 1
    return "-".join([a.title() for a in li])
