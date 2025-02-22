def solve() -> None:
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: BuzzFreeze")
        elif i % 3 == 0:
            print(f"{i}: Buzz")
        elif i % 5 == 0:
            print(f"{i}: Freeze")
        else:
            print(i)


if __name__ == "__main__":
    solve()