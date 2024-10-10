# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python

def good_vs_evil(good, evil):
    g, e = tuple(map(int, good.split(" "))), tuple(map(int, evil.split(" ")))

    good_value = sum((1 * g[0], 2 * g[1], 3 * g[2],
                      3 * g[3], 4 * g[4], 10 * g[5]))
    evil_value = sum((1 * e[0], 2 * e[1], 2 * e[2], 2 * e[3],
                      3 * e[4], 5 * e[5], 10 * e[6]))

    if good_value > evil_value:
        return "Battle Result: Good triumphs over Evil"
    if evil_value > good_value:
        return "Battle Result: Evil eradicates all trace of Good"
    return "Battle Result: No victor on this battle field"
