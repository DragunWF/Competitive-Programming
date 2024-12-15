# https://www.codewars.com/kata/59727ff285281a44e3000011/train/python

def band_name_generator(name: str) -> str:
    if name[0] == name[-1]:
        return f"{name.capitalize()}{name[1:]}"
    return f"The {name.capitalize()}"
