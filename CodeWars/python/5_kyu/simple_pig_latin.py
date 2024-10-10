# https://www.codewars.com/kata/520b9d2ad5c005041100000f

from string import punctuation as p

def pig_it(text):
    output = []
    for word in text.split(" "):
        output.append(word if word[0] in p else f"{word[1:]}{word[0]}ay")
    return " ".join(output)
