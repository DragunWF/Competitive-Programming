# https://www.codewars.com/kata/5803a6d8db07c59fff00015f/train/python

def starts_with(st: str, prefix: str) -> bool:
    # I'm not using the in-built startswith method here because it kinda defeats the purpose
    return st[:len(prefix)] == prefix
