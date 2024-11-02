for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    print("YES" if k >= n + 1 else "NO")