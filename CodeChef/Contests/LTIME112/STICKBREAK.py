for _ in range(int(input())):
    l, k = map(int, input().split(" "))
    print(0 if l % k == 0 else 1)