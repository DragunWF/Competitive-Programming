def solve() -> None:
    for _ in range(int(input())):
        x = int(input())
        while x > 3 or x % 2 == 0:
            if x > 3:
                x -= 3
            elif x % 2 == 0:
                x //= 2
        print(x)


if __name__ == "__main__":
    solve()
