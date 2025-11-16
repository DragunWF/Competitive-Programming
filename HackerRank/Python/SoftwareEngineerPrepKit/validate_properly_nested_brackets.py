# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/validate-properly-nested-brackets/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    opening_brackets = "({["
    closing_bracket_matches = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in code_snippet:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_bracket_matches:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if closing_bracket_matches[char] != opening_bracket:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
