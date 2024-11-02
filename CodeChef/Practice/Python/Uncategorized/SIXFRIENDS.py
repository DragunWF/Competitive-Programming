t = int(input())
for i in range(t):
    a, b = [int(n) for n in input().split(" ")]
    print(min((a * 3, b * 2)))