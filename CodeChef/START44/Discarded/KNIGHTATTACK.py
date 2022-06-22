# Yes I know... It's terrible. mainly because I was starting to panic when I saw
# that the timer was about to run out so I had no choice but to commit this sin...

t = int(input())
for i in range(t):
    c1 = tuple(map(int, input().split(" ")))
    c2 = tuple(map(int, input().split(" ")))

    check = False
    checks = (0, 2, 3, 4)
    for x in checks:
        for y in checks:
            if x == 0 and y == 3 or x == 3 and y == 0:
                continue
            if x == 4 and y == 3 or x == 3 and y == 4:
                continue
            if x == 2 and y == 3 or x == 3 and y == 2:
                continue
            if x == 2 and y == 4 or x == 4 and y == 2:
                continue
            if x == 2 and y == 0:
                continue
            if ((c1[0] + x == c2[0] and c1[1] + y == c2[1]) or
               (c1[0] - x == c2[0] and c1[1] - y == c2[1])):
                check = True
        if check:
            break

    checks = (1, 3)
    for x in checks:
        for y in checks:
            if x == y and x != 3:
                continue
            if ((c1[0] + x == c2[0] and c1[1] + y == c2[1]) or
               (c1[0] - x == c2[0] and c1[1] - y == c2[1])):
                check = True

    if (c1[0] - 1 == c2[0] and c1[1] - 1 == c2[1]) or c1[0] + 1 == c2[0] and c1[1] + 1 == c2[1]:
        check = True

    print("YES" if check else "NO")

# 5, 5
# 4, 4

# 7, 5
# 8, 4

# 4, 2
# 5, 1

# 7, 1
# 8, 2

# checks = ((1, 1), (-1, -1), (2, 0), (3, -1),
#           (-1, -3), (0, -4), (2, -4), (3, -3))

    # for pos in checks:
    #     x, y = c1[0] + pos[0], c1[1] + pos[1]
    #     if x == c2[0] and y == c2[1]:
    #         check = True
    #         break
    #     x, y = c1[0] - pos[0], c1[1] - pos[1]
    #     if x == c2[0] and y == c2[1]:
    #         check = True
    #         break
