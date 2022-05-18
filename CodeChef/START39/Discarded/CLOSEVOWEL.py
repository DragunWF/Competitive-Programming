import math

t = int(input())
for i in range(t):
    vowels = ("a", "e", "i", "o", "u")
    n = int(input())
    w = set(tuple(input()))
    count = 0
    for c in w:
        if c in vowels:
            count += 1
    print(math.floor(n / count))
