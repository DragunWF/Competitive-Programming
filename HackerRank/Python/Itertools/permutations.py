# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

if __name__ == "__main__":
    values = input().split(" ")
    s, k = values[0], int(values[1])
    for permutation in sorted(permutations(s, k)):
        print("".join(permutation))