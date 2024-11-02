# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AVGPROBLEM

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split(" "))
        print("YES" if (a + b) / 2 > c else "NO")
