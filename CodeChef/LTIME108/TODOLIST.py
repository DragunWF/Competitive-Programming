t = int(input())
for i in range(t):
    c = int(input())
    p = [int(n) for n in input().split(" ")]
    y = 0
    for r in p:
        if r >= 1000:
            y += 1
    print(y)
