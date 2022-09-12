for _ in range(int(input())):
    a, b, x, y = map(int, input().split(" "))
    if a / b == x / y:
        print("Equal")
    elif a / b > x / y:
        print("Alice")
    else:
        print("Bob")