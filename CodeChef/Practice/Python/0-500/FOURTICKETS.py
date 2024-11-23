# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FOURTICKETS

def solve():
    t = int(input())
    for _ in range(t):
        x = int(input())
        print("YES" if x * 4 <= 1000 else "NO")


if __name__ == "__main__":
    solve()