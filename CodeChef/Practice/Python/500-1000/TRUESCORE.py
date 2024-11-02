# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRUESCORE

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split(" "))
        c, d = map(int, input().split(" "))
        print("POSSIBLE" if c >= a and d >= b else "IMPOSSIBLE")
