# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

def remove_char(s):
    string = [*s]
    string.pop(0), string.pop(-1)
    return "".join(string)
