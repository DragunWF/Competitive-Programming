# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COUGAME

def solve() -> None:
    for _ in range(int(input())):
        g, b = map(int, input().split())
        print(b - g)


if __name__ == "__main__":
    solve()
