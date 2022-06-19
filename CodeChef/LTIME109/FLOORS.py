from math import ceil
t = int(input())
for i in range(t):
    x, y = map(int, input().split(" "))
    print(abs(ceil((x / 10)) - ceil((y / 10))))
