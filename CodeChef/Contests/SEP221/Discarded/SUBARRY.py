for _ in range(int(input())):
    input()
    arr = tuple(map(int, input().split(" ")))
    max_num, min_num = max(arr), min(arr)
    if min_num * max_num < min_num * min_num:
        print(f"{min_num * max_num} {max_num * max_num}")
    else:
        print(f"{min_num * min_num} {max_num * max_num}")
