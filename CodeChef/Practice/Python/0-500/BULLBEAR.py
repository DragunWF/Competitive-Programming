# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BULLBEAR

def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split(" "))
        if x > y:
            print("LOSS")
        elif x < y:
            print("PROFIT")
        else:
            print("NEUTRAL")


if __name__ == "__main__":
    solve()