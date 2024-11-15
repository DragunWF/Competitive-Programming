# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CANDIVIDE

t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if (n / 3) % 1 == 0 else "NO")
