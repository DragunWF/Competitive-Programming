# https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python

def vowel_indices(word):
    vowels = ("a", "e", "i", "o", "u", "y")
    indexes = []
    for i in range(len(word)):
        if word[i].lower() in vowels:
            indexes.append(i + 1)
    return indexes
