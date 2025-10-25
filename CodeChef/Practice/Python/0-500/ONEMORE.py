# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ONEMORE

def solve() -> None:
    for _ in range(int(input())):
        x = int(input())
        print("YES" if x > 24 else "NO")


if __name__ == "__main__":
    solve()
