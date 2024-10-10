# https://www.codewars.com/kata/56598d8076ee7a0759000087

from math import ceil


def calculate_tip(amount, rating):
    match (rating.lower()):
        case "terrible":
            return 0
        case "poor":
            return ceil(amount * 0.05)
        case "good":
            return ceil(amount * 0.1)
        case "great":
            return ceil(amount * 0.15)
        case "excellent":
            return ceil(amount * 0.2)
    return "Rating not recognised"
