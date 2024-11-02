# https://www.codewars.com/kata/565f448e6e0190b0a40000cc/train/python

def actually_really_good(foods: list[str]) -> str:
    if not foods:
        return "You know what's actually really good? Nothing!"
    if len(foods) == 1:
        return f"You know what's actually really good? {foods[0].capitalize()} and more {foods[0].lower()}."
    return f"You know what's actually really good? {foods[0].capitalize()} and {foods[1].lower()}."
