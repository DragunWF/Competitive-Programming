def solve() -> None:
    n = int(input("Enter height: "))
    cups = 0
    for i in range(1, n + 1):
        cups += i
    print(f"Number of cups needed: {cups}")


if __name__ == "__main__":
    solve()
