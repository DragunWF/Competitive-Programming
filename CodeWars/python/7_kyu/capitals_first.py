# https://www.codewars.com/kata/55c353487fe3cc80660001d4/train/python

def capitals_first(text: str) -> str:
    lowercase_words = []
    capitalized_words = []
    for word in text.split(" "):
        if not word[0].isalpha():
            continue
        elif word[0] == word[0].upper():
            capitalized_words.append(word)
        else:
            lowercase_words.append(word)
    return f'{" ".join(capitalized_words)} {" ".join(lowercase_words)}'.strip()


def test() -> None:
    print(capitals_first("hey You, Sort me Already!"))


if __name__ == "__main__":
    test()
