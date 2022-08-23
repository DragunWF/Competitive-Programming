def solve(a, b):
    return "A" if a > b else "B"

t = int(input())
for i in range(t):
    a, b = [int(n) for n in input().split(" ")]
    print(solve(a, b))