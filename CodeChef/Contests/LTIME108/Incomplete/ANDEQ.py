def search(arr):
    for i in range(len(arr)):
        if arr[i]:
            return i

t = int(input())
for i in range(t):
    x, m = int(input()), 0
    arr = list(map(int, input().split(" ")))
    temp_arr = arr
    while len(set(temp_arr)) != 1:
        m += 1
        index = search(arr)
        temp_arr[index - 1] = temp_arr[index - 1] & temp_arr[index]
        temp_arr.pop(index)
    print(m)

# Unsolved & Incomplete
