# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINFLIPS

def solve() -> None:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        if n % 2 != 0:
            print(-1)
            continue

        negative_sum = 0
        positive_sum = 0
        for i in range(n):
            if arr[i] > 0:
                positive_sum += arr[i]
            else:
                negative_sum += arr[i]

        print(max(positive_sum, abs(negative_sum)) - n // 2)


if __name__ == "__main__":
    solve()
