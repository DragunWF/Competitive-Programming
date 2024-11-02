# https://cses.fi/problemset/task/1070

if __name__ == '__main__':
    N = int(input())
    arr = [n for n in range(1, N + 1)]
    if N == 1:
        print("1")
    elif 2 <= N <= 3:
        print("NO SOLUTION")
    elif N == 4:
        print("2 4 1 3")
    else:
        for i in range(1, N + 1, 2):
            print(i, end=" ")
        for i in range(2, N + 1, 2):
            print(i, end=" ")
