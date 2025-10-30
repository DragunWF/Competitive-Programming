# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LTIME

def solve() -> None:
    for _ in range(int(input())):
        x = int(input())
        print("yes" if 1 <= x <= 4 else "no")


if __name__ == "__main__":
    solve()
