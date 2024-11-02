# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/HELIUM3\

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a, b, x, y = map(int, input().split(" "))
        print("YES" if x * y >= a * b else "NO")
