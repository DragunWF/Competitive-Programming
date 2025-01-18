def solve() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        students = list(map(int, input().split(" ")))
        seen_scores = set()
        for i in range(n):
            print("1" if all(
                students[i] > score for score in seen_scores) else "0", end=" "
            )
            seen_scores.add(students[i])
        print()


if __name__ == '__main__':
    solve()
