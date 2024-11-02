# https://cses.fi/problemset/task/1083

if __name__ == "__main__":
    n = int(input())
    expected_total = 0
    for i in range(1, n + 1):
        expected_total += i
    print(expected_total - sum(map(int, input().split(" "))))
