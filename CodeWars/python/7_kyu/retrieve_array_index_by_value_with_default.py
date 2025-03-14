# https://www.codewars.com/kata/515ceaebcc1dde8870000001/train/python

def solution(items: list, index: int, default_value):
    if not items or index < -len(items) or index >= len(items):
        return default_value
    return items[index]
