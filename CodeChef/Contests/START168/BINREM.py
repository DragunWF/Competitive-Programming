# Not finished

def solve() -> None:
    t = int(input())
    for _ in range(t):
        n, x, k = map(int, input().split(" "))
        s = input()
        ones = 0
        zeros = 0
        for char in s:
            if char == "1":
                ones += 1
            else:
                zeros += 1


if __name__ == '__main__':
    solve()
