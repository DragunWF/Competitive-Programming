# https://www.codewars.com/kata/59ad7d2e07157af687000070/train/python

def sentencify(words: list[str]) -> str:
    words[0] = f"{words[0][0].upper()}{words[0][1:]}"
    return f'{" ".join(words)}.'