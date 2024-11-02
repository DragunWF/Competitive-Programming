# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFSCORE

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split(" "))
        if y == 0:
            print("YES")
        elif x > y:
            print("NO")
        else:
            required = y / x
            print("YES" if required % 1 == 0 and required <= n else "NO")
