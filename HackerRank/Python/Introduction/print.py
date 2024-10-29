# https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    print("".join(str(i) for i in range(1, n + 1)))