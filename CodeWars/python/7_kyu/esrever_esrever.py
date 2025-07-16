# https://www.codewars.com/kata/57e0206335e198f82b00001d/train/python

def esrever(s: str) -> str:
    if not s:
        return ""

    words = s[:-1].split(" ")
    ending_punctuation_mark = s[-1]
    reversed_sentence_words = []
    for word in reversed(words):
        reversed_sentence_words.append(word[::-1])
    return " ".join(reversed_sentence_words) + ending_punctuation_mark


def test() -> None:
    print(esrever("world is amazing!"))  # "dlrow si gnizama!"


if __name__ == "__main__":
    test()
