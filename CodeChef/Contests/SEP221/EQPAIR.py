from collections import Counter
for _ in range(int(input())):
    input()
    arr = tuple(map(int, input().split(" ")))
    good_pairs = 0
    for n in Counter(arr).values():
        if n > 1:
            good_pairs += ((1 + n) / 2) * n - n
    print(int(good_pairs))
