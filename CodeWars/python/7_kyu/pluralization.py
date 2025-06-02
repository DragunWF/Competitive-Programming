# https://www.codewars.com/kata/57fe7ea808d102a2ba000edd/train/python

def pluralize(word: str) -> str:
    plural_rules_es = ("s", "x", "z", "ch", "sh")
    for rule in plural_rules_es:
        if word.endswith(rule):
            return f"{word}es"
    consonants = "bcdfghjklmnpqrstvwxyz"
    for consonant in consonants:
        if word.endswith(f"{consonant}y"):
            return f"{word[0:-1]}ies"
    return f"{word}s"


def test() -> None:
    print(pluralize("fly"))  # flies


if __name__ == "__main__":
    test()
