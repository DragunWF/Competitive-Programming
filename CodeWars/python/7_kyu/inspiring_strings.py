# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python

def longest_word(string_of_words):
    words = string_of_words.split(" ")
    words.reverse()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word