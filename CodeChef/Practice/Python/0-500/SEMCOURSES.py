# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SEMCOURSES

def solve() -> None:
    for _ in range(int(input())):
        x, y, z = map(int, input().split())
        print(x * y * z)


if __name__ == "__main__":
    solve()
