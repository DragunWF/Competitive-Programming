# https://www.codewars.com/kata/55147ff29cd40b43c600058b/train/python

def char_concat(word: str) -> str:
    output = ""
    for i in range(len(word) // 2):
        opposite = -(i + 1)
        output += f"{word[i]}{word[opposite]}{i + 1}"
    return output
