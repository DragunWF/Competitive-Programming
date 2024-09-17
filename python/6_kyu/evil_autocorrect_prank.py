# https://www.codewars.com/kata/538ae2eb7a4ba8c99b000439/train/python

from string import punctuation


def autocorrect(input: str) -> str:
    words = input.split(" ")
    output = []
    for word in words:
        new_word = autocorrect_word(word)
        if new_word != word and word[-1] in punctuation:
            new_word += word[-1]
        output.append(new_word)
    return " ".join(output)


def autocorrect_word(input: str) -> str:
    if input.lower().startswith("you"):
        for i in range(3, len(input)):
            if input[i] != "u" and input[i] != "U" and not input[i] in punctuation:
                break
        else:
            return "your sister"
        return input
    return "your sister" if input == "u" else input
