# https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2/train/python

def solution(pairs: dict):
    return ",".join([f"{key} = {pairs[key]}" for key in pairs])
