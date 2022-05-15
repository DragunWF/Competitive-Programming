t = int(input())
for i in range(t):
    m = list(map(int, input().split(" ")))[1]
    arr = sorted(set(map(int, input().split(" "))), reverse=True)
    sorted_tup = (arr[0], arr[1])
    max_sum = 0
    for x in sorted_tup:
        for y in sorted_tup:
            r = x + y + ((x - y) % m)
            if r > max_sum:
                max_sum = r
    print(max_sum)

# print(f"{numX} + {numY} + (({numX} - {numY}) mod {m}) = {r}")
