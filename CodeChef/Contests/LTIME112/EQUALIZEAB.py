for _ in range(int(input())):
    a, b, x = map(int, input().split(" "))
    if a == b or abs(a - b) % x == 0 and ((a // x) + (b // x)) % 2 == 0:
        print("YES")
    else:
        print("NO")
