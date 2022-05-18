t = int(input())
for i in range(t):
    x, y = map(int, input().split(" "))
    count = 0
    while x < y:
        count += 1
        x += 8
    print(count)