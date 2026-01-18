# https://www.codewars.com/kata/54598e89cbae2ac001001135/train/python

def any_(lst, func):
    return any(func(item) for item in lst)
