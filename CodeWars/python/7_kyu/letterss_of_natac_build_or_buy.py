# https://www.codewars.com/kata/59e6aec2b2c32c9d8b000184/train/python

def build_or_buy(hand: str) -> list:
    output = []
    b_count = hand.count("b")
    w_count = hand.count("w")
    g_count = hand.count("g")
    s_count = hand.count("s")
    o_count = hand.count("o")
    if b_count >= 1 and w_count >= 1:
        output.append("road")
        if s_count >= 1 and g_count >= 1:
            output.append("settlement")
    if o_count >= 3 and g_count >= 2:
        output.append("city")
    if o_count >= 1 and s_count >= 1 and g_count >= 1:
        output.append("development")
    return output
