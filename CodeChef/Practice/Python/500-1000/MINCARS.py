# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINCARS

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print((n / 4).__ceil__())
