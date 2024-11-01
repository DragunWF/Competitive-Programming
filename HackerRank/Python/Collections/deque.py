# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

if __name__ == "__main__":
    N = int(input())
    queue = deque()
    for i in range(N):
        args = input().split(" ")
        if args[0] == "append":
            queue.append(args[1])
        elif args[0] == "appendleft":
            queue.appendleft(args[1])
        elif args[0] == "pop":
            queue.pop()
        elif args[0] == "popleft":
            queue.popleft()
    print(" ".join(queue))
