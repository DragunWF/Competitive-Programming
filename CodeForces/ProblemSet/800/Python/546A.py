def solve(k, n, w):
    tp = 0
    for i in range(w):
        tp += k * (i + 1)
    r = tp - n
    return 0 if r < 0 else r


def main():
    k, n, w = map(int, input().split(" "))
    print(solve(k, n, w))


main()
