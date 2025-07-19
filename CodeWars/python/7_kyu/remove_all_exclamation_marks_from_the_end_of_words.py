# https://www.codewars.com/kata/57faf32df815ebd49e000117/train/python

def remove(s: str) -> str:
    words = s.split(" ")
    sentence = []
    for word in words:
        trimmed_word = word
        while trimmed_word.endswith("!"):
            trimmed_word = trimmed_word[0:-1]
        sentence.append(trimmed_word)
    return " ".join(sentence)


def test() -> None:
    print(remove("hi!!! !!hi hello!"))


if __name__ == "__main__":
    test()
