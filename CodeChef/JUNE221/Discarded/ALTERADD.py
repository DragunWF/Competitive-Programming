t = int(input())
for i in range(t):
    a, b = map(int, input().split(" "))
    ith = 1
    while a < b:
        a += 1 if ith % 2 > 0 else 2
        ith += 1
    print("YES" if a == b else "NO")

# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split(" "))
#     e = False
#     for j in range(b - a):
#         x = j // 2 * 2
#         y = j - j // 2
#         r = x + y
#         if r == b:
#             e = True
#             break
#         if r > b:
#             break
#     print("YES" if e else "NO")

# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split(" "))
#     e = False
#     for j in range(b - a + 1):
#         if a == b:
#             e = True
#             break
#         if a > b:
#             break
#         a += 2 if (j + 1) % 2 == 0 else 1
#     print("YES" if e else "NO")