# https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == "__main__":
    input()
    english_subs = set(input().split(" "))
    input()
    french_subs = set(input().split(" "))
    print(len(english_subs | french_subs))
