# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == "__main__":
    input()  # X
    sizes = Counter(map(int, input().split(" ")))
    N = int(input())
    money_earned = 0
    for i in range(N):
        size, money = map(int, input().split(" "))
        if size in sizes and sizes[size] > 0:
            sizes[size] -= 1
            money_earned += money
    print(money_earned)
