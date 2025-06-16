# https://www.codewars.com/kata/5a2b7edcb6486a856e00005b/train/python

def check_vowel(s: str, position: str) -> bool:
    return 0 <= position <= len(s) and s.lower()[position] in "aeiou"
