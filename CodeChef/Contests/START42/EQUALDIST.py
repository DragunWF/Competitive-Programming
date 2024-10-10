t = int(input())
for i in range(t):
    a, b = map(int, input().split(" "))
    print("YES" if (a + b) % 2 == 0 else "NO")
