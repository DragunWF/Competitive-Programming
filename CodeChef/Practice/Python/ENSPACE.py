t = int(input())
for i in range(t):
    n, x, y = map(int, input().split(" "))
    print("YES" if n >= x + y * 2 else "NO")
