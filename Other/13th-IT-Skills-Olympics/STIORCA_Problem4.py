def solve() -> None:
    n = int(input("Enter a positive integer: ")) # Positive Integer Only
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        steps += 1
        print(str(steps) + ':'+str(n))
    print(f"Total steps to reach 1: {steps}")


if __name__ == "__main__":
    solve()