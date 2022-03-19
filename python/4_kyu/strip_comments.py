# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(string, markers):
    output = []
    for stripped in string.split("\n"):
        for mark in markers:
            while mark in stripped:
                stripped = stripped[:stripped.index(mark)].strip()
        output.append(stripped)
    return "\n".join(output)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
