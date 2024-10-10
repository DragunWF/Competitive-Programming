def solve(s, t):
    r = [*s]
    r.reverse()
    r = "".join(r)
    return "YES" if r == t else "NO"


def main():
    s, t = input(), input()
    print(solve(s, t))


main()
