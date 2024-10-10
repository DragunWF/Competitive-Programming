# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    new_text = ""
    alphabets = ([*"abcdefghijklmnopqrstuvwxyz"])
    for letter in text.lower():
        if letter in alphabets:
            position = alphabets.index(letter)
            new_text += f"{position + 1} "
    return new_text.rstrip()
