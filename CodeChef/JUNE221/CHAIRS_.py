t = int(input())
for i in range(t):
    x, y = map(int, input().split(" "))
    print(abs(y - x) if x >= y else 0)
