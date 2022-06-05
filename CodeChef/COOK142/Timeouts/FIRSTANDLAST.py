import numpy
t = int(input())
for i in range(t):
    arr_length = int(input())
    a = map(int, input().split(" "))
    max_sum = 0
    for i in range(arr_length):
        sum = a[0] + a[-1]
        if sum > max_sum:
            max_sum = sum
        a = numpy.roll(a, -1)
    print(max_sum if arr_length > 1 else a[0])
