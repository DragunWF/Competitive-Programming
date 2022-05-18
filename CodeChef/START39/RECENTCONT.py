t = int(input())
for i in range(t):
    n = int(input())
    codes = tuple(map(int, input().split(" ")))
    print(f"{codes.count('START38')} {codes.count('LTIME108')}")
