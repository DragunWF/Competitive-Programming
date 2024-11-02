# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/JENGA

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split(" "))
        print("YES" if (x / n) % 1 == 0 else "NO")
