def solve(n, k):
    if n == 1 and k == 1:
        return "YES"
    r = int(((1 + k) / 2) * k)
    return "YES" if n >= r else "NO"


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split(" "))
        print(solve(n, k))


main()
