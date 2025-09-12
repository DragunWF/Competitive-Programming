# https://www.codewars.com/kata/599db0a227ca9f294b0000c8/train/python

def test(r: list) -> list:
    total_score = 0
    marks = {"h": 0, "a": 0, "l": 0}
    for score in r:
        total_score += score
        if score <= 6:
            marks["l"] += 1
        elif score <= 8:
            marks["a"] += 1
        else:
            marks["h"] += 1

    output = [round(total_score / len(r), 3), marks]
    if marks["a"] == 0 and marks["l"] == 0 and marks["h"] >= 1:
        output.append("They did well")
    return output
