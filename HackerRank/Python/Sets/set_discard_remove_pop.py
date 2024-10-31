# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

# Set to Python 3 not PyPy 3

if __name__ == '__main__':
    input()
    values = set(map(int, input().split(" ")))
    N = int(input())
    for i in range(N):
        args = input().split(" ")
        if args[0] == "pop" and len(values):
            values.pop()
        elif args[0] == "remove" and int(args[1]) in values:
            values.remove(int(args[1]))
        elif args[0] == "discard":
            values.discard(int(args[1]))
    print(sum(values))
