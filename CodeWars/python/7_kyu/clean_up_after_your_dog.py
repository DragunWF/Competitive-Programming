# https://www.codewars.com/kata/57faa6ff9610ce181b000028/train/python

def crap(garden: list[list[str]], bags: int, cap: int) -> str:
    poop = 0
    for area in garden:
        if "D" in area:
            return "Dog!!"
        poop += area.count("@")
    return "Cr@p" if poop > bags * cap else "Clean"
