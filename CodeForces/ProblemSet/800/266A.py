def solve(n, s):
    operations = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            operations += 1
    return operations


def main():
    n, s = int(input()), input()
    print(solve(n, s))


main()
