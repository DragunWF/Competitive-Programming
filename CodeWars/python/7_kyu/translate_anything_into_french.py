# https://www.codewars.com/kata/57238e345b21bb8c4b0000fc/train/python

def i_speak_french(sentence: str) -> str:
    if not sentence:
        return ""
    words = sentence.split(" ")
    translated_words = []
    for i, word in enumerate(words):
        is_last_word = i == len(words) - 1 or word[-1] == "."
        is_first_word = i == 0 or (i - 1 >= 0 and words[i - 1][-1] == ".")
        translated_words.append("Baguette" if is_first_word else "baguette")
        if is_last_word:
            translated_words.append("Encore!")
    return " ".join(translated_words)


def test() -> None:
    # Expected: "Baguette Encore!"
    print(i_speak_french("DragunWF"))

    # Expected: "Baguette baguette baguette Encore! Baguette baguette Encore!
    print(i_speak_french("I am fluent. In French."))


if __name__ == "__main__":
    test()
