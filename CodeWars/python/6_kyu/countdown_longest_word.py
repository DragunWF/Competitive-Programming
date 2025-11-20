# https://www.codewars.com/kata/57a4c85de298a795210002da

from collections import Counter

# Preloaded from the kata
words = ["GAME", "AAA2", "MAMG", "VAMPIRE", "FOX", "MOONSHINE"]


def longest_word(letters: str) -> list[str]:
    target_letter_freq = Counter(letters)
    chosen_words = []
    for word in words:
        if can_be_formed(target_letter_freq, word):
            chosen_words.append(word)
    return get_longest_word(chosen_words)


def get_longest_word(chosen_words: list[str]) -> list[str]:
    if not chosen_words:
        return None
    longest_len = max([len(word) for word in chosen_words])
    longest_words = []
    for word in chosen_words:
        if len(word) == longest_len:
            longest_words.append(word)
    longest_words.sort()
    return longest_words


def can_be_formed(letter_pool_counter: Counter, target_word: str) -> bool:
    target_word_counter = Counter(target_word)
    for letter in target_word_counter:

        if not letter in letter_pool_counter or letter_pool_counter[letter] < target_word_counter[letter]:
            return False
    return True


def test() -> None:
    print(longest_word("POVMERKIA"))  # ["VAMPIRE"]


if __name__ == "__main__":
    test()
