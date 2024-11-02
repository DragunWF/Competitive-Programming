# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NIBBLE

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print("good" if (n / 4) % 1 == 0 else "not good")
