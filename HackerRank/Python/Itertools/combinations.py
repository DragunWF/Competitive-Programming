# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

if __name__ == "__main__":
    values = input().split(" ")
    s, k = values[0], int(values[1])
    for i in range(1, k + 1):
        for combination in sorted(list(sorted(i) for i in combinations(s, i))):
            print("".join(combination))