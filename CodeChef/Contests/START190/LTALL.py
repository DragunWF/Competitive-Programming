def solve() -> None:
    for _ in range(int(input())):
        n = int(input())
        s = [*input()]
        lights = [digit == "1" for digit in s]
        for i in range(n):
            if lights[i]:
                if i != 0 and s[i - 1] == "0":
                    s[i - 1] = "1"
                elif i != n - 1 and s[i + 1] == "0":
                    s[i + 1] = "1"
        print("Yes" if all(digit == "1" for digit in s) else "No")


if __name__ == "__main__":
    solve()
