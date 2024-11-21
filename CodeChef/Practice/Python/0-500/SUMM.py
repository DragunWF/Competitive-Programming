# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUMM

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split(" "))
        print("YES" if a + b == c else "NO")


if __name__ == "__main__":
    solve()