# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

def series_sum(n):
    if not n:
        return "0.00"
    total = 1
    for i in range(2, n + 1):
        total += 1 / ((i - 1) * 3 + 1);
    return str("{0:.2f}".format(total))