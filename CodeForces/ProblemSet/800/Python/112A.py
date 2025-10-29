# https://codeforces.com/problemset/problem/112/A

def solve() -> None:
    a = input().lower()
    b = input().lower()
    if a == b:
        print(0)
        return

    values = [a, b]
    values.sort()
    print(1 if values[1] == a else -1)


if __name__ == "__main__":
    solve()
