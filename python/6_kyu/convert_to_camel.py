# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    output = []
    capitalize = False
    for chr in text:
        if chr == "-" or chr == "_":
            capitalize = True
        else:
            output.append(chr.upper() if capitalize else chr)
            capitalize = False
    return "".join(output)
