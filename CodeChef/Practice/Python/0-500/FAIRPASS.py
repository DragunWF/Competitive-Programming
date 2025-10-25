# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FAIRPASS

def solve() -> None:
    for _ in range(int(input())):
        n, k = map(int, input().split())
        print("yes" if k > n else "no")


if __name__ == "__main__":
    solve()
