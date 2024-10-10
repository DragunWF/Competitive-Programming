# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrev_name(name):
    prev, output = " ", ""
    for chr in name:
        if prev == " ":
            output += chr.upper()
        prev = chr
    return f"{output[0]}.{output[1]}"
