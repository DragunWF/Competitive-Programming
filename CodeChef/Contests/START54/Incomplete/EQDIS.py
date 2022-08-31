from collections import Counter


def solve(n, a):
    counter, distinct = Counter(a).values(), 0
    for value in counter:
        if value <= 2:
            distinct += value
        else:
            return "NO"
    return "YES" if distinct % 2 == 0 else "NO"


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = tuple(map(int, input().split(" ")))
        print(solve(n, a))


main()
