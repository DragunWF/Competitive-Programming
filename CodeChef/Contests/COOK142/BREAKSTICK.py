t = int(input())
for i in range(t):
    n, x = map(int, input().split(" "))
    b = False
    if n % 2 == 0 or x == 1:
        b = True
    if n % 2 != 0 and x % 2 != 0:
        b = True
    print("YES" if b else "NO")
