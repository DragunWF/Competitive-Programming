# https://www.codewars.com/kata/58f6f87a55d759439b000073

def negation_value(s: str, val: bool) -> bool:
    output = s.count("!") % 2 == 0
    return output if val else not output
