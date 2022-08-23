t = int(input())
for i in range(t):
    arr_length = int(input())
    a = tuple(map(int, input().split(" ")))

    if arr_length <= 2:
        print(sum(a))
    else:
        max_sum = 0

        for i in range(arr_length):
            sum = max(a[i] + a[i - 1], a[i] + a[i + 1]
                      if i + 1 != arr_length else a[i] + a[0])
            if sum > max_sum:
                max_sum = sum

        print(max_sum)
