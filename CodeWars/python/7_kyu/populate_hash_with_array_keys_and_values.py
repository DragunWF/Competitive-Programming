# https://www.codewars.com/kata/51c38e14ea1c97ffaf000003/train/python

def populate_dict(keys: list[str], default) -> dict:
    output = {}
    for key in keys:
        output[key] = default
    return output
