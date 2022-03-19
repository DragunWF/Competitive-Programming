# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

from string import punctuation as p
from string import ascii_letters as letters


def top_3_words(text: str) -> list:
    data, top, array = {}, [], []

    for chr in [x for x in [*p] if x != "'"]:
        while chr in text:
            text = text.replace(chr, " ")

    for element in [x for x in text.lower().split(" ") if len(x)]:
        is_word = True
        if "'" in element:
            is_word = False
            for chr in element:
                if chr in letters:
                    is_word = True
                    break

        if is_word:
            array.append(element)

    for word in array:
        if not word in [i for i in data]:
            data[word] = 0
        else:
            data[word] += 1

    s = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    for x in range(3 if len(data) > 3 else len(data)):
        top.append([k for k in s][-1 - x])

    return top


print(top_3_words("  , e   .. "))

# def top_3_words(text: str) -> list:
#     data, top, array = {}, [], []

#     for chr in [x for x in [*p] if x != "'"]:
#         text.replace(chr, " ")
#     text = text.lower().split(" ")

#     for w in text:
#         new_str = []

#         for i in range(len(w)):
#             if len(w[i]):
#                 if not w[i] in [*p]:
#                     new_str.append(w[i])
#                 else:
#                     if w[i] != w[-1] and not w[i + 1] in [*p] and not w[i - 1] in [*p]:
#                         new_str.append(w[i])

#         if len(new_str):
#             array.append("".join(new_str))

#     for w in array:
#         if not w in [i for i in data]:
#             data[w] = 0
#         else:
#             data[w] += 1

#     s = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
#     for x in range(3 if len(data) > 3 else len(data)):
#         top.append([k for k in s][-1 - x])

#     return top
