# https://www.codewars.com/kata/559f44187fa851efad000087/train/python

def seven_ate9(s: str) -> str:
    output = s[0]
    for i in range(1, len(s) - 1):
        if s[i - 1] == "7" and s[i] == "9" and s[i + 1] == "7":
            continue
        output += s[i]
    output += s[-1]
    return output
