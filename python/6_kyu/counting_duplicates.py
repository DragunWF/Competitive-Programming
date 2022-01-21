# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    uniques, duplicates = [], []
    for ltr in text.lower():
        if ltr not in uniques:
            uniques.append(ltr)
        elif ltr in uniques:
            if ltr not in duplicates:
                duplicates.append(ltr)
                uniques.pop(uniques.index(ltr))
    return len(duplicates)
