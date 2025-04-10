# https://www.codewars.com/kata/567de8823fa5eee02100002a/train/python

def whitespace(text: str) -> bool:
    whitespaces = (" ", "\t", "\n", "\r", "\f", "\v")
    return all(char in whitespaces for char in text)
