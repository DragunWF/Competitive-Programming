t = int(input())
for i in range(t):
    a, b, c = map(int, input().split(" "))
    r = max(a, b, c)
    if r == a:
        print("Alice")
    if r == b:
        print("Bob")
    if r == c:
        print("Charlie")
