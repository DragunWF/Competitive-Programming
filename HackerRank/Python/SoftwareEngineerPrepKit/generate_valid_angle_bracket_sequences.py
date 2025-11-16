# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/generate-valid-angle-bracket-sequences/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(n):
    solution = []
    answer = []
    def generateSolutions(openCount, closeCount):
        if len(solution) == 2 * n:
            answer.append("".join(solution))
            return
        if openCount < n:
            solution.append("<")
            generateSolutions(openCount + 1, closeCount)
            solution.pop()
        if openCount > closeCount:
            solution.append(">")
            generateSolutions(openCount, closeCount + 1)
            solution.pop()
    generateSolutions(0, 0)
    return answer

if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
