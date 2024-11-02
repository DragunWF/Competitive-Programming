# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SUBSCRIBE_

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split(" "))
        print((n / 6).__ceil__() * x)
