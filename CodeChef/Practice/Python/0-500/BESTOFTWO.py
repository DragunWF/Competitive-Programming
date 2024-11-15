# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BESTOFTWO

t = int(input())
for _ in range(t):
    x, y = map(int, input().split(" "))
    print(max(x, y))