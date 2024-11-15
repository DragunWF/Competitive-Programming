# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MINHEIGHT

t = int(input())
for _ in range(t):
    x, h = map(int, input().split(" "))
    print("YES" if x >= h else "NO")