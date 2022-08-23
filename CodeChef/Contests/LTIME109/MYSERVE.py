from math import ceil
t = int(input())
for i in range(t):
    p, q = map(int, input().split(" "))
    turns = ceil((p + q + 1) / 2)
    print("Alice" if turns % 2 != 0 else "Bob")
