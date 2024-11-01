# https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        try:
            a, b = map(int, input().split(" "))
            print(a // b)
        except ValueError as e:
            print(f"Error Code: {e}")
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")