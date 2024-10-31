# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        a = set(input().split(" "))
        input()
        b = set(input().split(" "))
        print(a.issubset(b))
