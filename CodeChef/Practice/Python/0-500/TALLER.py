# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TALLER

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split(" "))
        print("A" if x > y else "B")
