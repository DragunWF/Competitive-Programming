def solve(m, n):
    return (m * n) // 2


def main():
    m, n = map(int, input().split(" "))
    print(solve(m, n))


main()
