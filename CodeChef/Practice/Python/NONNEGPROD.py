def array_product(arr):
    product = arr[0]
    for i in range(1, len(arr)):
        product *= arr[i]
    return product


def solve(a):
    ans = 0
    while array_product(a) < 0:
        for i in range(len(a)):
            if a[i] < 0:
                a.pop(i)
                break
        ans += 1
    return ans


def main():
    for _ in range(int(input())):
        input()
        a = list(map(int, input().split(" ")))
        print(solve(a))


main()
