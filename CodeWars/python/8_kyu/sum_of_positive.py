# https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
    new_arr = []
    for number in arr:
        if number > 0:
            new_arr.append(number)
    return sum(new_arr)
