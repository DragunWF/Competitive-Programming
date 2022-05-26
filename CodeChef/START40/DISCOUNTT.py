t = int(input())
for i in range(t):
    n, x, y = map(int, input().split(" "))
    a = tuple(map(int, input().split(" ")))
    t = sum(a)
    d = sum(tuple([n - y if n - y >= 0 else 0 for n in a]))
    print("COUPON" if d + x < t else "NO COUPON")
