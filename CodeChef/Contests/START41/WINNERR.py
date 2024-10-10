t = int(input())
for i in range(t):
    pa, pb, qa, qb = map(int, input().split(" "))
    p, q = max(pa, pb), max(qa, qb)
    if p == q:
        print("TIE")
    else:
        print("P" if p < q else "Q")
