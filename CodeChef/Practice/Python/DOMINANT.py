def solve(a, b, c):
    if a > b + c:
        return "YES"
    if b > a + c:
        return "YES"
    if c > a + b:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    a, b, c = [int(n) for n in input().split(" ")]
    print(solve(a, b ,c))