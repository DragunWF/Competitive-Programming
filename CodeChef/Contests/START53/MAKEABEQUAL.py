t = int(input())
for i in range(t):
    n = int(input())
    a = tuple(map(int, input().split(" ")))
    b = tuple(map(int, input().split(" ")))
    if (sum(a) == sum(b)):
        operations = 0
        for i in range(n):
            operations += abs(a[i] - b[i])
        print(operations // 2)
    else:
        print(-1)
