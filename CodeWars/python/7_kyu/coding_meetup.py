# https://www.codewars.com/kata/582746fa14b3892727000c4f/train/python

def count_developers(lst: list) -> int:
    js_developers = 0
    for developer in lst:
        if developer["language"] == "JavaScript" and developer["continent"] == "Europe":
            js_developers += 1
    return js_developers
