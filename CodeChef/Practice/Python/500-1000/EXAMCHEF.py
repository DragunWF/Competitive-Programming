# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/EXAMCHEF

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x, y, z = map(int, input().split(" "))
        print("YES" if z > (x * y) / 2 else "NO")
