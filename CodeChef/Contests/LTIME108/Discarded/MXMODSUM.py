t = int(input())
for i in range(t):
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    max_sum = 0
    for numX in arr:
        for numY in arr:
            r = numX + numY + ((numX - numY) % m)
            if r > max_sum:
                max_sum = r
    print(max_sum)