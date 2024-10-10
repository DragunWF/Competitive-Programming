t = int(input())
for i in range(t):
    k, x = map(int, input().split(" "))
    days = k * 7 - x
    print(days if days > 0 else 0)
