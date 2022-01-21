# https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    pos, neg = [x for x in arr if x > 0], [y for y in arr if y < 0]
    return [len(pos), sum(neg)] if arr else arr
