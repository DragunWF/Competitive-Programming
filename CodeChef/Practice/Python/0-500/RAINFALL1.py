# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RAINFALL1

def solve() -> None:
    for _ in range(int(input())):
        x = int(input())
        if x < 3:
            print("LIGHT")
        elif 3 <= x < 7:
            print("MODERATE")
        else:
            print("HEAVY")


if __name__ == "__main__":
    solve()
