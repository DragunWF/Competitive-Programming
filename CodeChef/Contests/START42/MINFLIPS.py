t = int(input())
for i in range(t):
    arr_len = int(input())
    arr = list(map(int, input().split(" ")))
    pos = tuple(filter(lambda x: x == 1, arr))
    if arr_len % 2 != 0:
        print(-1)
    else:
        arr_sum = abs(len(pos) - arr_len // 2)
        print(-1 if arr_sum < 0 else arr_sum)
