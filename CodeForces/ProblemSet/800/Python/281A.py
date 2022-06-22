def solve(s):
    return f"{s[0].upper()}{s[1::]}"


def main():
    s = input()
    print(solve(s))


main()
