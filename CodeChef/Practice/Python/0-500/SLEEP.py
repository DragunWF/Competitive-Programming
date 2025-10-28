# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SLEEP

def solve() -> None:
    for _ in range(int(input())):
        x = int(input())
        print("yes" if x < 7 else "no")


if __name__ == "__main__":
    solve()
