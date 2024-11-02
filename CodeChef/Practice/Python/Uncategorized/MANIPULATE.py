t = int(input())
for i in range(t):
    x, y = [int(n) for n in input().split(" ")]
    print("YES" if x >= y else "NO")