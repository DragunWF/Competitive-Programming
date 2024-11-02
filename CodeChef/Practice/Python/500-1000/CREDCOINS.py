# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CREDCOINS

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split(" "))
        print((y * x) // 100)
