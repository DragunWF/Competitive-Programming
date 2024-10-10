# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python

import re


def get_order(order):
    menu = ("burger", "fries", "chicken", "pizza",
            "sandwich", "onionrings", "milkshake", "coke")
    output = []
    for food in menu:
        found: list[str] = re.findall(food, order)
        for item in found:
            output.append(item.capitalize())
    return " ".join(output)
