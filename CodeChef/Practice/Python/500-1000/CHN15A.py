# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHN15A


def solve() -> None:
    for _ in range(int(input())):
        wolverine_like_minions = 0
        n, k = map(int, input().split())
        values = list(map(int, input().split()))
        for i in range(n):
            if (values[i] + k) % 7 == 0:
                wolverine_like_minions += 1
        print(wolverine_like_minions)


if __name__ == "__main__":
    solve()
