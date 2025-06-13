# https://www.codewars.com/kata/66d85e2db4d3909a8d0b53c9

def is_cyrillic(letter):
    return letter in ''.join(chr(i) for i in range(0x0400, 0x0500))
