# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WAITTIME

def solve() -> None:
    for _ in range(int(input())):
        k, x = map(int, input().split())
        print(k * 7 - x)


if __name__ == "__main__":
    solve()
