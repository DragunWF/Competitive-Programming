# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-valid-anagram/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def isAnagram(s, t):
    return int("".join(sorted(s)) == "".join(sorted(t)))

if __name__ == '__main__':
    s = input()

    t = input()

    result = isAnagram(s, t)

    print(result)
