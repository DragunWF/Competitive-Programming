# https://www.codewars.com/kata/56b8903933dbe5831e000c76

def spoonerize(words: str) -> str:
    words = words.split()
    first_word = [*words[0]]
    last_word = [*words[-1]]

    temp_first_word_letter = first_word[0]
    first_word[0] = last_word[0]
    last_word[0] = temp_first_word_letter

    words[0] = "".join(first_word)
    words[-1] = "".join(last_word)

    return " ".join(words)


def test() -> None:
    # Expected: pot nicking
    print(spoonerize("not picking"))


if __name__ == "__main__":
    test()
