# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANAPTS

def solve() -> None:
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(y // x)


if __name__ == "__main__":
    solve()
