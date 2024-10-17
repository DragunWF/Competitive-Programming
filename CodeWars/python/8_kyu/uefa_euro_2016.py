# https://www.codewars.com/kata/57613fb1033d766171000d60/train/python

def uefa_euro_2016(teams, scores):
    INTRO = f"At match {teams[0]} - {teams[1]}, "
    if scores[0] == scores[1]:
        return f"{INTRO}teams played draw."
    return f"{INTRO}{teams[0] if scores[0] > scores[1] else teams[1]} won!"
