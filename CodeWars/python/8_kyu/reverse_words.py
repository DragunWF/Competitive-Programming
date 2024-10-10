# https://www.codewars.com/kata/51c8991dee245d7ddf00000e

def reverse_words(s):
    s = s.split()
    s.reverse()
    return " ".join(s)
