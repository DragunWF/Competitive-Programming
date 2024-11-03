# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/POLYBAGS

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print((n / 10).__ceil__())