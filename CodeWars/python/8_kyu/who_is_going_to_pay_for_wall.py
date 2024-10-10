# https://www.codewars.com/kata/58b28e5830473070e5000007/train/python

def who_is_paying(name):
    return [name] if len(name) <= 2 else [name, name[0:2]]
