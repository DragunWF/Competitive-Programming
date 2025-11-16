# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-non-identical-string-rotation/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    if s1 == s2 or len(s1) != len(s2):
        return 0
    return s1 in f"{s2}{s2}"


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
