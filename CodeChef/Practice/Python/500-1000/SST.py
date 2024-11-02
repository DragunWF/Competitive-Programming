# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SST

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split(" "))
        a_value, b_value = a * 10, b * 5
        if a_value > b_value:
            print("FIRST")
        elif a_value < b_value:
            print("SECOND")
        else:
            print("ANY")
