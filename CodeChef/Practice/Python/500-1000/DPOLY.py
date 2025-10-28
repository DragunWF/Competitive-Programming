# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DPOLY

def solve() -> None:
    for _ in range(int(input())):
        n = int(input())
        values = list(map(int, input().split()))
        for i in range(n - 1, -1, -1):
            if values[i] != 0:
                print(i)
                break


if __name__ == "__main__":
    solve()
