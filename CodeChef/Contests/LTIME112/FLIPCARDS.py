for _ in range(int(input())):
    n, x = map(int, input().split(" "))
    print(min(n, x, abs(n - x)))