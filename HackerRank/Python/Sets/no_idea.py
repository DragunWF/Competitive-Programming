# https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    input()
    arr = input().split(" ")
    a = set(input().split(" "))
    b = set(input().split(" "))
    happiness = 0
    for n in arr:
        if n in a:
            happiness += 1
        elif n in b:
            happiness -= 1
    print(happiness)