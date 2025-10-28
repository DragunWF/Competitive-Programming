# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/RECENTCONT

def solve() -> None:
    for _ in range(int(input())):
        n = int(input())
        start38_problems = 0
        ltime108_problems = 0
        values = input().split()
        for i in range(n):
            if values[i] == "START38":
                start38_problems += 1
            else:
                ltime108_problems += 1
        print(f"{start38_problems} {ltime108_problems}")


if __name__ == "__main__":
    solve()
