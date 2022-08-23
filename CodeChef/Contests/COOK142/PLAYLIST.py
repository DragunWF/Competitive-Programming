t = int(input())
for i in range(t):
    n, x = map(int, input().split(" "))
    print(n // (x * 3))
