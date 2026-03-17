# https://www.codewars.com/kata/5a21f943c5e284d4340000cb/train/python

def debug(s: str) -> str:
    filtered_plural = s.replace("bugs", "+++")
    filtered_bugs = filtered_plural.replace("bug", "")
    return filtered_bugs.replace("+++", "bugs")
