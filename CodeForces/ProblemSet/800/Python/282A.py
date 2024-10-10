def solve(t):
    x = 0
    for i in range(t):
        s = input()
        x += 1 if "+" in s else -1
    return x


def main():
    t = int(input())
    print(solve(t))


main()
