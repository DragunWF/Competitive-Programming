# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SALE

def solve() -> None:
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        min_value = min(a, b, c)
        is_min_read = False
        total = 0
        for num in [a, b, c]:
            if min_value == num and not is_min_read:
                is_min_read = True
                continue
            total += num
        print(total)


if __name__ == "__main__":
    solve()
