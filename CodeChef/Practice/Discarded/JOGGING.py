for _ in range(int(input())):
    n, x = map(int, input().split(" "))
    for i in range(n - 1):
        x += x
    print(x % (10 ** 9 + 7))
