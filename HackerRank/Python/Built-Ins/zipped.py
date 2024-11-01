# https://www.hackerrank.com/challenges/zipped/problem

if __name__ == "__main__":
    N, X = map(int, input().split(" "))
    grades = [[] for i in range(N)]
    for i in range(X):
        report = map(float, input().split(" "))
        for i, grade in enumerate(report):
            grades[i].append(grade)
    for i in range(N):
        print(float(round(sum(grades[i]) / len(grades[i]), 1)))