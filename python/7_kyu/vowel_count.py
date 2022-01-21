# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels, ltr_cnt = [*"aeiou"], 0
    for ltr in sentence.lower():
        if ltr in vowels:
            ltr_cnt += 1
    return ltr_cnt
