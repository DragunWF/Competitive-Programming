t = int(input())
for i in range(t):
    x, y = map(int, input().split(" "))
    if y >= x:
        print(y - x)
    else:
        a = (x + y) % 2 == 0
        print((x - y) // 2 if a else
              (x + 1 - y) // 2 + 1)

# ---------------------------------------------------------------

# Previous attempts

# Too Slow (Correct but algorithm is inefficient)
# t = int(input())
# for i in range(t):
#     x, y = map(int, input().split(" "))
#     operations = 0
#     while x != y:
#         operations += 1
#         if x < y:
#             x += 1
#         else:
#             y += 2
#     print(operations)

# Wrong Answer
# t = int(input())
# for i in range(t):
#     x, y = map(int, input().split(" "))
#     print(y - x if y >= x else (x - y) // 2)
