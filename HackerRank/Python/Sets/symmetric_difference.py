# https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    input()
    a = set(map(int, input().split(" ")))
    input()
    b = set(map(int, input().split(" ")))
    for num in sorted(a ^ b):
        print(num)
