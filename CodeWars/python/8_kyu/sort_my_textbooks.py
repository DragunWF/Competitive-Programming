# https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python

def sorter(textbooks: list) -> list:
    textbooks.sort(key=lambda item: item.lower())
    return textbooks
