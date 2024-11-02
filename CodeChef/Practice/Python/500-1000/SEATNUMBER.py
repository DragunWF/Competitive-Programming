# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SEATNUMBER

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        if n <= 10:
            print("Lower Double")
        elif n <= 15:
            print("Lower Single")
        elif n <= 25:
            print("Upper Double")
        else:
            print("Upper Single")
