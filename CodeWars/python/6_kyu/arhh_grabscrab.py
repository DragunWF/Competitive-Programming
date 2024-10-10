# https://www.codewars.com/kata/52b305bec65ea40fe90007a7/train/python

def grabscrab(said: str, possible_words: list[str]) -> str:
    output, said_letters = [], sorted(said)
    for word in possible_words:
        if sorted(word) == said_letters:
            output.append(word)
    return output
