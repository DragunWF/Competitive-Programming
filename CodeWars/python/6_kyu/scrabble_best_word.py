# https://www.codewars.com/kata/563f960e3c73813942000015/train/python

import math
from string import ascii_lowercase as letters


def get_best_word(points, words):
    min_len, max_value, target_index = math.inf, -math.inf, 0
    for i, str in enumerate(words):
        current_value, current_len = get_value(points, str), len(str)
        if current_value > max_value or current_value == max_value and current_len < min_len:
            target_index = i
            max_value = current_value
            min_len = current_len
    return target_index


def get_value(points, word: str):
    word = word.lower()
    total = 0
    for char in word:
        total += points[letters.index(char)]
    return total


# Test code
points = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 10, 1, 2,
          1, 1, 3, 8, 1, 1, 1, 1, 4, 10, 10, 10, 10)
test_cases = [["WHO", "IS", "THE", "BEST", "OF", "US"],  # 0
              ["AABCDEF", "WHO", "IS", "THE", "BEST", "OF", "US"],  # 1
              ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG']]  # 5
for i, case in enumerate(test_cases):
    print(get_best_word(points, case))
