# https://www.codewars.com/kata/5467e4d82edf8bbf40000155

def descending_order(num):
    li, new_li = [int(x) for x in [*str(num)]], []
    for i in range(len(li)):
        new_li.append(str(max(li)))
        li.pop(li.index(max(li)))
    return int("".join(new_li))
