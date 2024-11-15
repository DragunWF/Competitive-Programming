# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRIZEPOOL

t = int(input())
for _ in range(t):
    x, y = map(int, input().split(" "))
    print(10 * x + 90 * y)
