def solve(x, h):
    return "YES" if x >= h else "NO"

t = int(input())
for i in range(t):
    x, h = [int(n) for n in input().split(" ")]
    print(solve(x, h))