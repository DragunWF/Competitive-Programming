# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

# Set interpreter to Pypy 3

if __name__ == "__main__":
    input()  # n will not be used
    print(hash(tuple(map(int, input().split(" ")))))
