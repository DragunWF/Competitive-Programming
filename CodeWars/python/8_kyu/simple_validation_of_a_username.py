# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/train/python

from string import ascii_lowercase, digits

def validate_usr(username):
    allowed = ascii_lowercase + digits + "_"
    if not 4 <= len(username) <= 16:
        return False
    for char in username:
        if not char in allowed:
            return False
    return True