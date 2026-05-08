# https://www.codewars.com/kata/580a0347430590220e000091/train/python

from typing import Union
from math import sqrt


def area(d: int, l: int) -> Union[float, int, str]:
    return l * sqrt(d ** 2 - l ** 2) if d > l else "Not a rectangle"
