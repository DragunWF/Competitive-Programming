# https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/train/python

def calculate(s: str) -> int:
    sentence = s.split(" ")
    modifier = int(sentence[-1])
    operation = sentence[-2]
    fruit_count = 0
    for item in sentence:
        if item.isdigit():
            fruit_count = int(item)
            break
    return fruit_count + modifier if operation == "gains" else fruit_count - modifier
