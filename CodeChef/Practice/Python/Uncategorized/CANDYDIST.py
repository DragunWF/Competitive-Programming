t = int(input())
for i in range(t):
    n, m = map(int, input().split(" "))
    print("Yes" if (n / m) % 2 == 0 else "No")
