# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CARTRIP

def solve() -> None:
    for _ in range(int(input())):
        x = int(input())
        print(max(300 * 10, x * 10))


if __name__ == "__main__":
    solve()
