# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUBSCRIBE

def solve():
    t = int(input())
    for _ in range(t):
        x = int(input())
        print("YES" if x > 30 else "NO")


if __name__ == "__main__":
    solve()