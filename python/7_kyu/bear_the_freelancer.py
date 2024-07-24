# https://www.codewars.com/kata/58d5b39b1c0402c5f7002e0d/train/python

def bear_dollars(jobs: list) -> int:
    prices, total = {"close friend": 25, "friend": 50, "acquaintance": 100}, 0
    for hours, client in jobs:
        total += prices[client.lower()] * hours if client.lower() in prices else hours * 125
    return total
