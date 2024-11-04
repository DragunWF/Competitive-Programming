# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PRESENTS

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(n - n // 5)