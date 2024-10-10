# https://www.codewars.com/kata/60dda5a66c4cf90026256b75/train/python

def some_but_not_all(seq, pred):
    result = [pred(element) for element in seq]
    return any(result) and not all(result)
