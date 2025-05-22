# https://www.codewars.com/kata/5996eb39cdc8eb39f80000a0/train/python

from decimal import Decimal, ROUND_HALF_UP


def round_by_2_decimal_places(n: Decimal) -> Decimal:
    return n.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
