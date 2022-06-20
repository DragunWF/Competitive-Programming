def solve(w):
    if w != 2 and w % 2 == 0:
        return "YES"
    return "NO"


def main():
    w = int(input())
    print(solve(w))


main()
