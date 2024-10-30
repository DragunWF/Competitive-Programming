# https://www.codewars.com/kata/6627696c86b953001280675e/train/python

def deemojify(emote_string: str) -> str:
    chains = emote_string.split("  ")
    emojis = {
        ":)": 0,
        ":D": 1,
        ">(": 2,
        ">:C": 3,
        ":/": 4,
        ":|": 5,
        ":O": 6,
        ";)": 7,
        "^.^": 8,
        ":(": 9
    }
    output = ""
    for chain in chains:
        str_num = ""
        for emoji in chain.split(" "):
            str_num += str(emojis[emoji])
        output += chr(int(str_num))
    return output
