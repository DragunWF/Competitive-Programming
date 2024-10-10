def solve(x):
    output = sorted(x.split("+"))
    return "+".join(output)


def main():
    x = input()
    print(solve(x))


main()
