t = int(input())
for i in range(t):
    frames = int(input())
    n = input().split(" ")
    last_item = None
    arr = []
    for item in n:
        if item != last_item:
            last_item = item
            arr.append(item)
    print(len(arr))
