t = int(input())
for i in range(t):
    arr_length = int(input())
    a = tuple(map(int, input().split(" ")))
    sums = []
    for i in range(arr_length):
        sums.append(a[i] + a[i + 1] if i + 1 != arr_length
                    else a[i] + a[0])
    print(max(sums) if arr_length > 1 else a[0])
