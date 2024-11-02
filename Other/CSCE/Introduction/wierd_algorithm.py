# https://cses.fi/problemset/task/1068/

if __name__ == '__main__':
    n = int(input())
    print(n, end=" ")
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
        print(n, end=" ")
