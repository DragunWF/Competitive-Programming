# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/OFFICE

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split(" "))
        print(x * 4 + y)
