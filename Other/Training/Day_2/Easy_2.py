import sys


def solve() -> None:
    word = input("Word: ")
    print("Vowel count: ", count_vowels((word)))


def count_vowels(word: str) -> int:
    VOWELS = "aeiou"
    count = 0
    for char in word.lower():
        if char in VOWELS:
            count += 1
    return count


if __name__ == "__main__":
    solve()