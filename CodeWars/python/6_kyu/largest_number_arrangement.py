# https://www.codewars.com/kata/59d902f627ee004281000160/solutions/python

from itertools import permutations

def largest_arrangement(numbers):
    possible_nums = []
    for permutation in permutations(numbers):
        possible_nums.append(int("".join(str(n) for n in permutation)))
    return max(possible_nums)