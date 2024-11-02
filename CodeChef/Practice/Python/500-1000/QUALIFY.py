# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/QUALIFY

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x, a, b = map(int, input().split(" "))
        print("Qualify" if a + b * 2 >= x else "NotQualify")
