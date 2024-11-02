# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINPIZZA

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split(" "))
        print((n * x / 4).__ceil__())
