# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/M1ENROL

def solve() -> None:
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(max(0, y - x))


if __name__ == "__main__":
    solve()
