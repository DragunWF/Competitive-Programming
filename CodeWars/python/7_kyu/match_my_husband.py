# https://www.codewars.com/kata/5750699bcac40b3ed80001ca/train/python

def match(usefulness: list[int], months: int) -> str:
    total_usefulness = sum(usefulness)
    WOMAN_NEEDS = 100 * ((1 - 0.15) ** months)
    return "Match!" if total_usefulness >= WOMAN_NEEDS else "No match!"
