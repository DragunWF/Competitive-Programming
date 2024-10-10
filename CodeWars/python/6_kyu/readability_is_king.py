# https://www.codewars.com/kata/52b2cf1386b31630870005d4

import re


def flesch_kincaid(text: str) -> float:
    words_list = text.lower().split(" ")
    syllables, words = 0, len(words_list)
    sentences = len(re.split("[.?!]", text)[:-1])
    for word in words_list:
        syllables += count_syllables(word)
    return round((0.39 * (words / sentences)) + (11.8 * (syllables / words)) - 15.59, 2)


def count_syllables(word: str) -> int:
    VOWELS = "aeiou"
    syllable_count = 0
    inside_vowel_group = False
    for char in word:
        if char in VOWELS and not inside_vowel_group:
            inside_vowel_group = True
            syllable_count += 1
        else:
            inside_vowel_group = False
    return syllable_count


def test():
    # Not part of the solution, just testing
    print(flesch_kincaid("The turtle is leaving."))


if __name__ == "__main__":
    test()
