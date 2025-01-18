# https://www.codewars.com/kata/52f3bb2095d6bfeac2002196/train/python

def valid_word(seq: list[str], word: str) -> bool:
    if not word:
        return True
    for root_word in seq:
        if word.startswith(root_word):
            if valid_word(seq, word[len(root_word):]):
                return True
    return False
