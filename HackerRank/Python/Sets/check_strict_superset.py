# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

if __name__ == '__main__':
    a = set(input().split(" "))
    N = int(input())
    is_strict_superset = True
    for i in range(N):
        s = set(input().split(" "))
        if not (a.issuperset(s) and len(a - s) >= 1):
            is_strict_superset = False
    print(is_strict_superset)