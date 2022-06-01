x = int(input())
a, b = [int(n) for n in input().split(" ")]
print("Yes" if x >= b + a else "No")
