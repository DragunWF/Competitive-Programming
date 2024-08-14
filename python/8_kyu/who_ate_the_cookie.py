# https://www.codewars.com/kata/55a996e0e8520afab9000055

def cookie(x):
    INPUT_TYPE, OUTPUT_TEXT = type(x), "Who ate the last cookie? It was"
    if INPUT_TYPE is str:
        return f"{OUTPUT_TEXT} Zach!"
    if INPUT_TYPE is float or INPUT_TYPE is int:
        return f"{OUTPUT_TEXT} Monica!"
    return f"{OUTPUT_TEXT} the dog!"
