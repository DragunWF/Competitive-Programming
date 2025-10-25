# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/READPAGES

def solve() -> None:
    for _ in range(int(input())):
        n, x, y = map(int, input().split())
        print("yes" if x * y >= n else "no")


if __name__ == "__main__":
    solve()
