# https://www.codewars.com/kata/57241cafef90082e270012d8/train/python

from string import ascii_lowercase


def keyword_cipher(plain_text: str, keyword: str) -> str:
    cipher_map = create_cipher_map(keyword)
    output = ""
    for char in plain_text.lower():
        if not char in cipher_map:
            output += char
            continue
        ascii_pos = ascii_lowercase.index(char)
        output += cipher_map[ascii_pos]
    return output


def create_cipher_map(keyword: str) -> str:
    cipher_map = []
    for char in (keyword.lower() + ascii_lowercase):
        if not char in cipher_map:
            cipher_map.append(char)
    return cipher_map
