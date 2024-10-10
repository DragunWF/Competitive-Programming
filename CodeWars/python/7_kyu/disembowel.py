# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    vowels = ([*"aeiouAEIOU"])
    word = ""
    for letter in string_:
        for x in range(10):
            if letter == vowels[x]:
                break
        else:
            word += letter
    string_ = word
    return string_
