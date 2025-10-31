# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTRDSGN

def solve() -> None:
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        print(min(x1 + y1, x2 + y2))


if __name__ == "__main__":
    solve()
