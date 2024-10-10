def solve(x):
    x = [int(n) for n in x.split(" ")]
    return "YES" if x[0] * x[1] <= x[2] else "NO"

t = int(input())
for i in range(t):
    x = input()
    print(solve(x))