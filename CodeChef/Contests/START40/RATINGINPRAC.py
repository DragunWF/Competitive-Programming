t = int(input())
for i in range(t):
    l = input()
    x = list(map(int, input().split(" ")))
    s = True
    for a, b in zip(sorted(x), x):
        if a != b:
            s = False
            break
    print("Yes" if s else "No")
