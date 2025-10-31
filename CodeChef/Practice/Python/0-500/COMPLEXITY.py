# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COMPLEXITY

def solve() -> None:
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print("yes" if x > y else "no")


if __name__ == "__main__":
    solve()
