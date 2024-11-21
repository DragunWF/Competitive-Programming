# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/REACHFAST

def solve():
    t = int(input())
    for _ in range(t):
        a, b, k = map(int, input().split(" "))
        print((abs(a - b) / k).__ceil__())


if __name__ == "__main__":
    solve()