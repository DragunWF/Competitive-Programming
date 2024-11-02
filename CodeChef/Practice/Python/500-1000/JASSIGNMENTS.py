# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/JASSIGNMENTS

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x = int(input())
        print("Yes" if x + 3 <= 10 else "No")
