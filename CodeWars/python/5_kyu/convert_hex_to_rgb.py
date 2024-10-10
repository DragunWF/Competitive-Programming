# https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python

def hex_string_to_RGB(hex_string: str):
    rgb, temp_hex = {"r": 0, "g": 0, "b": 0}, ""
    keys = tuple(rgb.keys())
    for i in range(1, len(hex_string)):
        temp_hex += hex_string[i].upper()
        if i % 2 == 0:
            rgb[keys[i // 2 - 1]] = convert_hex(temp_hex)
            temp_hex = ""
    return rgb


def convert_hex(value: str):
    hex = [*[str(n) for n in range(10)], *"ABCDEF"]
    return hex.index(value[1]) + hex.index(value[0]) * 16


# test code
print(hex_string_to_RGB("#beaded"))

# Better solution from other programmers
def hex_string_to_RGB2(hex_string):
    r = int(hex_string[1:3], 16)
    g = int(hex_string[3:5], 16)
    b = int(hex_string[5:7], 16)

    return {'r': r, 'g': g, 'b': b}
