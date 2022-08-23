t = int(input())
for i in range(t):
    n, x = map(int, input().split(" "))
    r = pow(x * 2, n) // 2
    print(r % 1000000007)

# Timeout...