def solve(n, k):
    for i in range(k):
        last_number = int(str(n)[-1])
        if last_number == 0:
            n = int(n / 10)
        else:
            n = int(n - 1)
    return n


def main():
    n, k = map(int, input().split(" "))
    print(solve(n, k))


main()
