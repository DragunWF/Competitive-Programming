# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DNATION

def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split(" "))
        print(abs(x - y))


if __name__ == "__main__":
    solve()