# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

from string import punctuation as p
from string import ascii_letters as letters


def top_3_words(text: str) -> list:
    data, top, array = {}, [], []

    for chr in [x for x in [*p] if x != "'"]:
        while chr in text:
            text = text.replace(chr, " ")

    for element in [x for x in text.lower().split(" ") if len(x)]:
        has_letters = any(chr in [*element] for chr in letters)
        if "'" in element and not has_letters: continue
        else: array.append(element)

    for word in array:
        if not word in [i for i in data]: data[word] = 0
        else: data[word] += 1

    s = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    for x in range(3 if len(data) > 3 else len(data)):
        top.append([k for k in s][-1 - x])

    return top


print(top_3_words("  //wont won't won't "))
