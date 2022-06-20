def solve(k, arr):
    participants_advanced = 0
    for score in arr:
        if score >= arr[k - 1] and score > 0:
            participants_advanced += 1
    return participants_advanced


def main():
    n, k = map(int, input().split(" "))  # Ignore n
    arr = tuple(map(int, input().split(" ")))
    print(solve(k, arr))


main()
