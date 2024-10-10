t = int(input())
for i in range(t):
    n = input()
    a = set([*input()])
    b = set([*input()])
    d = len(a) > len(b)
    r = tuple(filter(lambda x: not x in (b if d else a), a if d else b))
    print(len(r))

# t = int(input())
# for i in range(t):
#     n = int(input())
#     a, b = input(), input()
#     op = 0
#     ch = ""
#     for j in range(n):
#         if a[j] == b[j] or ch == b[j]:
#             continue
#         else:
#             ch = b[j]
#             op += 1
#     print(op)