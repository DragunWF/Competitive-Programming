# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WATERFILLING

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        b = map(int, input().split(" "))
        filled = 0
        for water in b:
            if water:
                filled += 1
        print("Water filling time" if filled <= 1 else "Not now")
