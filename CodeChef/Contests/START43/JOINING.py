from math import ceil
t = int(input())
for i in range(t):
    n, k = map(int, input().split(" "))
    g = ceil(n / 5)
    r = k // 5 + (1 if k % 5 != 0 else 0)
    print(g - r)
