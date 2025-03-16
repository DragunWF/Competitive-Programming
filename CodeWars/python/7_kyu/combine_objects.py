# https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819/train/python

def combine(*args: list[dict]) -> dict:
    output = {}
    for arg in args:
        for key in arg:
            if not key in output:
                output[key] = arg[key]
            else:
                output[key] += arg[key]
    return output
