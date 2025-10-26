# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BIN_BAT

def solve() -> None:
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        total_minutes = 0
        while True:
            n /= 2
            total_minutes += a
            if n == 1:
                break
            total_minutes += b
        print(total_minutes)


if __name__ == "__main__":
    solve()
