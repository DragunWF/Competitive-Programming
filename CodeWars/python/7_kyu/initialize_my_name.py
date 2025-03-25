# https://www.codewars.com/kata/5768a693a3205e1cc100071f/train/python

def initialize_names(name: str) -> str:
    words = name.split(" ")
    if len(words) <= 2:
        return name
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            continue
        words[i] = f"{word[0].upper()}."
    return " ".join(words)
