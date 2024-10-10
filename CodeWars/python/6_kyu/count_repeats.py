# https://www.codewars.com/kata/598ee7b6ec6cb90dd6000061/train/python

def count_repeats(txt):
    repeats = 0
    prev_char = None
    for char in txt:
        if prev_char == char:
            repeats += 1
        prev_char = char
    return repeats
