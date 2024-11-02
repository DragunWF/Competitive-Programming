# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NEARESTEXIT

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        x = int(input())
        print("LEFT" if x <= 50 else "RIGHT")
