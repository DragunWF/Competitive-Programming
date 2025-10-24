# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/T20MCH


def solve() -> None:
    r, o, c = map(int, input().split(" "))
    runs = (20 - o) * 6
    team_b_score = runs * 6
    print("YES" if c + team_b_score > r else "NO")


if __name__ == "__main__":
    solve()
