t = int(input())
for i in range(t):
    a, b = map(int, input().split(" "))
    d = b - a
    if d > 1:
        if d != 3:
            j = d - (d // 3 if d > 5 else d % 3)
        else:
            j = 2
        x = j // 2 * 2
        y = j - j // 2
        r = x + y
    else:
        r = 1
    print("YES" if a + r == b else "NO")
