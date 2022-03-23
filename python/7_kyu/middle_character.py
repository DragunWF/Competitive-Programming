# https://www.codewars.com/kata/56747fd5cb988479af000028/train/javascript

import math

def get_middle(string):
    index = math.floor(len(string) / 2)
    if len(string) % 2 == 0:
        return f"{string[index - 1]}{string[index]}"
    return string[index]


print(get_middle("test"))
