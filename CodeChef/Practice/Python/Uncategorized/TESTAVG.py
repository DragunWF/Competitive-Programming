t = int(input())
for i in range(t):
    scores = tuple(map(int, input().split(" ")))
    averages = ((scores[0] + scores[1]) / 2, (scores[0] + scores[2]) / 2,
                (scores[1] + scores[2]) / 2)
    fail = False
    for avg in averages:
        if avg < 35:
            fail = True
    print("Pass" if not fail else "Fail")
