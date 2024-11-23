# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SNDMAX

def solve():
    n = int(input())
    for _ in range(n):
        print(sorted(list(map(int, input().split(" "))))[1])


if __name__ == "__main__":
    solve()