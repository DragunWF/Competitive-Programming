# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/ACTEMP

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        a, b, c = map(int, input().split(" "))
        print("yes" if a <= b and c <= b else "no")
