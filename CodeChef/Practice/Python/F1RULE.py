def solve(y, x):
    return "YES" if x <= y * 1.07 else "NO"

t = int(input())
for i in range(t):
    x = [int(n) for n in input().split(" ")]
    print(solve(x[0], x[1]))