# https://www.codewars.com/kata/5269452810342858ec000951/train/python

import re

def is_valid_coordinates(coordinates: str) -> bool:
    if re.search(r"[^0-9\-., ]", coordinates):
        return False
    values = coordinates.split(",")
    if len(values) != 2:
        return False
    try:
        values = [float(n.strip()) for n in values]
        if not (-90 <= values[0] <= 90) or not (-180 <= values[1] <= 180):
            return False
    except ValueError:
        return False
    return True
