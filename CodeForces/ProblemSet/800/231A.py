def solve(t):
    solved_problems = 0
    for i in range(t):
        p = tuple(map(int, input().split(" ")))
        if p.count(1) >= 2:
            solved_problems += 1
    return solved_problems


def main():
    t = int(input())
    print(solve(t))


main()
