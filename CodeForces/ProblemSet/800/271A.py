def solve(y):
    while True:
        y += 1
        d = len(set([*str(y)]))
        if d == 4:
            return y


def main():
    y = int(input())
    print(solve(y))


main()
