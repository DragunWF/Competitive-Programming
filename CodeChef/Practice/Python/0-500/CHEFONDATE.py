# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEFONDATE

t = int(input())
for _ in range(t):
    x, y = map(int, input().split(" "))
    print("YES" if x >= y else "NO")
