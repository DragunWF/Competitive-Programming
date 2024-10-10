t = int(input())
for i in range(t):
    b = ("c", "g", "l", "r")
    n = int(input())
    s = input()
    rc = 0
    for c in s:
        if c in b:
            rc += 1
    print((2 ** rc) % ((10 ** 9) + 7) if rc else 1)
