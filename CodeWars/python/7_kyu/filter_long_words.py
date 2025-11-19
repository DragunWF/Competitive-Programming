# https://www.codewars.com/kata/5697fb83f41965761f000052

def filter_long_words(sentence: str, n: int) -> str:
    filtered_sentence = []
    words = sentence.split(" ")
    for word in words:
        if len(word) > n:
            filtered_sentence.append(word)
    return filtered_sentence


def test() -> None:
    print(filter_long_words("The quick brown fox jumps over the lazy dog", 4))


if __name__ == "__main__":
    test()
