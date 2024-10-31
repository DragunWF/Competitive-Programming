# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

if __name__ == '__main__':
    input()
    a = set(input().split(" "))
    N = int(input())
    for i in range(N):
        command = input().split(" ")[0]
        s = set(input().split(" "))
        if command == "update":
            a.update(s)
        elif command == "intersection_update":
            a.intersection_update(s)
        elif command == "symmetric_difference_update":
            a.symmetric_difference_update(s)
        elif command == "difference_update":
            a.difference_update(s)
    print(sum(int(n) for n in a))
