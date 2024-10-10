# https://www.codewars.com/kata/5168bb5dfe9a00b126000018

def solution(string):
    word = [*string]
    word.reverse()
    return "".join(word)
