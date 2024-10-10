t = int(input())
for i in range(t):
    a, b = map(int, input().split(" "))
    count = 0
    while True:
        if a % 3 == 0 or b % 3 == 0:
            break
        if a > b:
            a -= abs(b)
        else:
            b = abs(a - b)
        count += 1
    print(count)
