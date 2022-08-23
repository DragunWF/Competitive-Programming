w = map(int, input().split(" "))
c = 0
for n in w:
    if n >= 10:
        c += 1
print(c)
