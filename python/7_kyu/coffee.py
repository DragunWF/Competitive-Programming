# https://www.codewars.com/kata/595d54bddddd7cf91800008c/train/python

import re


def coffee(sentence: str) -> str:
    return re.sub("[Cc][Oo][Ff][Ff][Ee][Ee]", "COFFEE", sentence)
