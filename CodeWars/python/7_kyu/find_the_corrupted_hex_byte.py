# https://www.codewars.com/kata/6a54d3e91e9fb16ca31cc912/train/python

HEX = set("0123456789ABCDEF")


def find_corrupted_byte(dump: list) -> int:
    for i, byte in enumerate(dump):
        if len(byte) != 2 or not byte[0] in HEX or not byte[1] in HEX:
            return i
    return -1
