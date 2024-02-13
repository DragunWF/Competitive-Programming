# https://www.codewars.com/kata/5b097da6c3323ac067000036/train/python

def solve(a, b):
    alice, bob = 0, 0
    for score_a, score_b in zip(a, b):
        if score_a > score_b:
            alice += 1
        elif score_b > score_a:
            bob += 1
    score = f'{alice}, {bob}: '
    if alice > bob:
        return f'{score}Alice made "Kurt" proud!'
    if bob > alice:
        return f'{score}Bob made "Jeff" proud!'
    return f'{score}that looks like a "draw"! Rock on!'
