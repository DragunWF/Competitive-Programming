t = int(input())
for i in range(t):
    x, p, q = map(int, input().split(" "))
    r = (p - q) * x
    print(r if r >= 0 else 0)