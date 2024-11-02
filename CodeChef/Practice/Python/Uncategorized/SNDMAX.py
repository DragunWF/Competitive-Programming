def solve(x):
    x.pop(x.index(max(x)))
    return max(x)

t = int(input())
for i in range(t):
    x = [int(n) for n in input().split(" ")]
    print(solve(x))