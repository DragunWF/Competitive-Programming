t = int(input())
for i in range(t):
    n = int(input())
    a, b = input(), input()
    chr = []
    for j in range(n):
        if a[j] != b[j] and not b[j] in chr:
            chr.append(b[j])
    print(len(chr))
