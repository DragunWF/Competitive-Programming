# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFRACES

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y, a, b = map(int, input().split(" "))
        gold_medals = 0
        for race in (x, y):
            if not race in (a, b):
                gold_medals += 1
        print(gold_medals)