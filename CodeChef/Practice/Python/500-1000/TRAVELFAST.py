# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRAVELFAST

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split(" "))
        if x < y:
            print("BIKE")
        elif x > y:
            print("CAR")
        else:
            print("SAME")