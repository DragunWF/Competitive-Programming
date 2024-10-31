# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

if __name__ == "__main__":
    input()
    english = set(input().split(" "))
    input()
    french = set(input().split(" "))
    print(len(english - french))
