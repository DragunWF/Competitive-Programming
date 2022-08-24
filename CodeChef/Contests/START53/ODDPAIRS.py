t = int(input())
for i in range(t):
    n = int(input())
    x = n // 2
    if n % 2 == 0:
        print(x * x * 2)
    else:
        print(x * (n - x) * 2)
