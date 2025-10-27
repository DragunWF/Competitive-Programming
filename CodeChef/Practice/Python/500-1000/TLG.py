# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TLG

def solve() -> None:
    N = int(input())
    max_a_lead = 0
    max_b_lead = 0
    cumulative_a_score = 0
    cumulative_b_score = 0

    for _ in range(N):
        a, b = map(int, input().split())
        cumulative_a_score += a
        cumulative_b_score += b
        lead = cumulative_a_score - cumulative_b_score
        if lead < 0 and abs(lead) > max_b_lead:
            max_b_lead = abs(lead)
        elif lead > max_a_lead:
            max_a_lead = lead

    if max_a_lead > max_b_lead:
        print(f"1 {max_a_lead}")
    else:
        print(f"2 {max_b_lead}")


if __name__ == "__main__":
    solve()
