def solve(x):
    x = [int(n) for n in x.split(" ")]
    if not x[0] and not x[1]:
        return "NO"
    if x[0] == x[1]:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    x = input()
    print(solve(x))