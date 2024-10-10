import math
for _ in range(int(input())):
    n = int(input())
    if n <= 3:
        print(-1)
    elif n == 4:
        print("2 4 1 3")
    else:
        x = math.ceil(n / 2) + 1
        if n % 2 != 0:
            x -= 1
        for i in range(1, x):
            print(n // 2 + i, end=" ")
            print(i, end=" ")
        if n % 2 != 0:
            print(n, end=" ")
        print()

# Testing
# for _ in range(int(input())):
#     n = _ + 1
#     if n % 2 != 0 or n <= 4:
#         pass
#     else:
#         arr = []
#         for i in range(1, n // 2 + 1):
#             arr.append(i)
#             arr.append(n // 2 + i)
#         for x in range(len(arr) - 1):
#             if abs(arr[x + 1] - arr[x]) < 2:
#                 print(" ".join(tuple(map(str, arr))))
#                 break
