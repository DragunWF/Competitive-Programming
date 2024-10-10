# https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python

from string import ascii_lowercase


def words_to_marks(s):
    total = 0
    for char in s:
        total += ascii_lowercase.index(char) + 1
    return total


# Test code
print(words_to_marks('attitude'))
