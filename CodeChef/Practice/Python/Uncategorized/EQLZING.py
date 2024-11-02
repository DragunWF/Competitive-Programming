t = int(input())
for i in range(t):
    a, b = map(int, input().split(" "))
    print("Yes" if abs(a - b) % 2 == 0 else "No")