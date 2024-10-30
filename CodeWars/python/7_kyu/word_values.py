# https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python

from string import ascii_lowercase


def name_value(my_list: list[int]) -> list[int]:
    return [(i + 1) * get_word_value(my_list[i]) for i in range(len(my_list))]


def get_word_value(word: str) -> int:
    value = 0
    for char in word:
        if char in ascii_lowercase:
            value += ascii_lowercase.index(char) + 1
    return value
