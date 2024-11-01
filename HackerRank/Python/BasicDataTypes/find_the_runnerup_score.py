# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    input()
    print(sorted(list(set(map(int, input().split()))))[-2])
    