t = int(input())
for i in range(t):
    s_len = int(input()) - 1
    s = input()
    max_count = 0
    if s_len != 1:
        if s.find("011") == -1:
            for i in range(s_len):
                if i + 1 == s_len and s[i] == "0" and s[i - 1] == "0":
                    max_count += 1
                if i == 0 and s[i] == "1" and s[i + 1] == "1":
                    max_count += 1
        else:
            max_count += 1
    else:
        max_count += 1
    print(max_count)

# t = int(input())
# for i in range(t):
#     s_len = int(input()) - 1
#     s = input()
#     max_count = 0
#     if s_len != 1:
#         for i in range(s_len):
#             if i + 1 == s_len:  # if at last
#                 if s[i] == "0" and s[i - 1] == "0":
#                     max_count += 1
#                 elif s[i] == "1" and s[i - 1] == "0":
#                     max_count += 1
#             elif i == 0 and s[i] == "1" and s[i + 1] == "1":
#                 max_count += 1
#             elif i != 0 and i + 1 != s_len:  # if at middle
#                 if s[i] == "1" and s[i - 1] == "0" and s[i + 1] == "1":
#                     max_count += 1
#     else:
#         max_count += 1
#     print(max_count)
