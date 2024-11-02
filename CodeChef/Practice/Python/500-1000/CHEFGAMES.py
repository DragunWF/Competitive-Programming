# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFGAMES

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        r = map(int, input().split(" "))
        print("OUT" if any(r) else "IN")
