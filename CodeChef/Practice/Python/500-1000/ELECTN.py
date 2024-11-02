# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/ELECTN

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split(" "))
        ages = map(int, input().split(" "))
        eligible = 0
        for age in ages:
            if age >= x:
                eligible += 1
        print(eligible)
