from math import ceil


def solve() -> None:
    p = int(input("Enter the percentile threshold for passing: "))
    y = int(input("Enter your assumed score: "))
    n = int(input("Enter the number of students in your class: "))

    print("Enter the estimated scores of your classmates")
    estimated_scores = [y]
    for i in range(n - 1):
        estimated_scores.append(int(input()))
    estimated_scores.sort(reverse=True)

    passing_rank = ceil((p / 100) * n)
    passing_score = estimated_scores[passing_rank - 1]
    print("Verdict: PASS" if y >= passing_score else "Verdict: FAIL")


if __name__ == "__main__":
    solve()
