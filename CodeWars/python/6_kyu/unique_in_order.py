# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    uniques = [iterable[0]] if iterable else []
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i - 1]:
            uniques.append(iterable[i])
    return uniques