# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INVESTMENT

def solve() -> None:
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print("yes" if x >= y * 2 else "no")


if __name__ == "__main__":
    solve()
