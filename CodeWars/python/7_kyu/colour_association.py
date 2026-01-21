# https://www.codewars.com/kata/56d6b7e43e8186c228000637/train/python

def colour_association(arr: list[list[str, str]]) -> list[dict]:
    return [{item[0]: item[1]} for item in arr]
