def solve(s):
    length = len(s)
    if length > 10:
        return f"{s[0]}{length - 2}{s[-1]}"
    return s


def main():
    t = int(input())
    for i in range(t):
        s = input()
        print(solve(s))


main()
