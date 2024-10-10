def solve(s):
    a, d = 0, 0
    for win in s:
        if win == "A":
            a += 1
        else:
            d += 1
    if a == d:
        return "Friendship"
    return "Anton" if a > d else "Danik"


def main():
    n, s = input(), input()  # Ignore n
    print(solve(s))


main()
