# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEAT

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tuesdays = round(n / 7, 2)
        floating_val = str(tuesdays).split(".")[1]
        if float(floating_val) >= 28:
            tuesdays += 1
        print((tuesdays).__floor__())


if __name__ == "__main__":
    solve()