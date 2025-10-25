# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHESSTIME

def solve() -> None:
    for _ in range(int(input())):
        n = int(input())
        print(n * 60 // 20)


if __name__ == "__main__":
    solve()
