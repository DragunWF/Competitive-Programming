t = int(input())
for i in range(t):
    n = [*range(1, int(input()) + 1)]
    arr = []
    pick_last = True
    positive_index, negative_index = 0, -1
    for j in range(len(n)):
        if pick_last:
            arr.append(str(n[negative_index]))
            negative_index -= 1
        else:
            arr.append(str(n[positive_index]))
            positive_index += 1
        pick_last = False if pick_last else True
    arr.reverse()
    print(" ".join(arr))
