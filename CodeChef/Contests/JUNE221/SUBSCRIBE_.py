from math import ceil
t = int(input())
for i in range(t):
    n, x = map(int, input().split(" "))
    print(ceil((n / 6)) * x)
