from string import ascii_uppercase as uc
from string import ascii_lowercase as lc
from string import ascii_letters as ltrs
# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b


def same_case(a, b):
    if a in ltrs and b in ltrs:
        if a in lc and b in lc:
            return 1
        elif a in uc and b in uc:
            return 1
        else:
            return 0
    else:
        return -1
