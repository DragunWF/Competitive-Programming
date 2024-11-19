# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RIGHTTHERE

t = int(input())
for _ in range(t):
    n, x = map(int, input().split(" "))
    print("YES" if x >= n else "NO")
