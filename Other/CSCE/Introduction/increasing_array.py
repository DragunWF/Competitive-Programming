# https://cses.fi/problemset/task/1094

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(" ")))
    moves = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            result = arr[i - 1] - arr[i]
            moves += result
            arr[i] += result
    print(moves)
