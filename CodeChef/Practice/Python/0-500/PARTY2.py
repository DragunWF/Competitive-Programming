# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PARTY2

def solve() -> None:
    for _ in range(int(input())):
        n, x, k = map(int, input().split())
        print("yes" if n * x <= k else "no")


if __name__ == "__main__":
    solve()
