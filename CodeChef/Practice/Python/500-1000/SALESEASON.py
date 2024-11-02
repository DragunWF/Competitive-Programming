# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SALESEASON

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        x = int(input())
        if x <= 100:
            print(x)
        elif 100 < x <= 1000:
            print(x - 25)
        elif 1000 < x <= 5000:
            print(x - 100)
        else:
            print(x - 500)
