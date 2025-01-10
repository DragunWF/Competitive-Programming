# https://www.codewars.com/kata/5836ebe4f7e1c56e1a000033/train/python

def combine_strings(*args: list[str]) -> str:
    if not args:
        return ""
    if len(args) == 1:
        return args[0]

    output = ""
    max_len = max(len(arg) for arg in args)
    for i in range(max_len):
        for arg in args:
            if i < len(arg):
                output += arg[i]

    return output
