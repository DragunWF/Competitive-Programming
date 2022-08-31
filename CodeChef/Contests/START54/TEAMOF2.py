def solve(n):
    s = []
    for i in range(n):
        values = input()
        k = int(values[0])
        if k != 0:
            p = list(map(int, values[2:].split(" ")))
            s.append(p)

    for i in range(len(s)):
        pair = []
        for j in range(len(s)):
            if i != j:
                pair = [*s[i], *s[j]]
                if len(set(pair)) == 5:
                    return "YES"

    return "NO"


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(solve(n))


main()
