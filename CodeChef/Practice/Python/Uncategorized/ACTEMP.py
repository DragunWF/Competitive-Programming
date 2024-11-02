t = int(input())
for i in range(t):
    a, b, c = map(int, input().split(" "))
    print("No" if b < max(a, c) else "Yes")
