t = int(input())
for i in range(t):
    w, x, y, z = map(int, input().split())
    result = y * z + w
    if result == x:
        print("filled")
    if result < x:
        print("unfilled")
    if result > x:
        print("overflow")
