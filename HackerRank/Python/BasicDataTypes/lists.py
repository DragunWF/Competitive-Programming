# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        args = input().split(" ")
        command = args[0]
        # Forgive me father for I have sinned
        if command == "print":
            print(arr)
        elif command == "insert":
            num = [int(n) for n in args[1:]]
            arr.insert(num[0], num[1])
        elif command == "remove":
            arr.remove(int(args[1]))
        elif command == "append":
            arr.append(int(args[1]))
        elif command == "pop":
            arr.pop()
        elif command == "sort":
            arr.sort()
        elif command == "reverse":
            arr.reverse()
