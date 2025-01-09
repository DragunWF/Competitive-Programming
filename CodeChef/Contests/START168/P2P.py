def solve() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input()
        b = input()
        score = 0
        choice_counts = 0
        for i in range(n):
            if a[i] == "1" or b[i] == "1":
                if a[i] == "1" and b[i] == "1":
                    score += 1
                else:
                    choice_counts += 1
        if score % 2 != 0 or (score % 2 == 0 and choice_counts > 0):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()
