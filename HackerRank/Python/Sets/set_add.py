# https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == "__main__":
    n = int(input())
    distinct_countries = set()
    for i in range(n):
        country = input()
        distinct_countries.add(country)
    print(len(distinct_countries))