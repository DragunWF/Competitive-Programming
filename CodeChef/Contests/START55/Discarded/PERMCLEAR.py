for _ in range(int(input())):
    input()
    a = input().split(" ")
    input()
    b = input().split(" ")
    c = filter(lambda x: not x in b, a)
    print(" ".join(c))
