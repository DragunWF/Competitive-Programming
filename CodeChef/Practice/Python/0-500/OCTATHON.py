# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/OCTATHON

def solve() -> None:
    x = int(input())
    if x < 3:
        print("GOLD")
    elif x < 6:
        print("SILVER")
    else:
        print("BRONZE")


if __name__ == "__main__":
    solve()
