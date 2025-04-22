# https://www.codewars.com/kata/54eea36b7f914221eb000e2f/train/python

def sort_it(words: str, n: int) -> str:
    word_list = words.split(", ")
    trim = lambda item: "".join(item.split(" "))
    word_list.sort(key=lambda item: trim(item[n - 1]))
    return ", ".join(word_list)
