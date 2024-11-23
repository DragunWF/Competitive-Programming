# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHOPRT

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split(" "))
        if a > b:
            print(">")
        elif a < b:
            print("<")
        else:
            print("=")



if __name__ == "__main__":
    solve()