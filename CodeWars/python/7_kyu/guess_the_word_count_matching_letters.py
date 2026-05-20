# https://www.codewars.com/kata/5912ded3f9f87fd271000120/train/python

def count_correct_characters(correct: str, guess: str) -> int:
    if len(correct) != len(guess):
        raise Exception("Lengths are not the same!")
    count = 0
    for i, char in enumerate(correct):
        if char == guess[i]:
            count += 1
    return count
