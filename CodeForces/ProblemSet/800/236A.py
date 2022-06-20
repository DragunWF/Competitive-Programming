def solve(s):
    return ("IGNORE HIM!" if len(set([*s])) % 2 != 0
            else "CHAT WITH HER!")


def main():
    s = input()
    print(solve(s))


main()
