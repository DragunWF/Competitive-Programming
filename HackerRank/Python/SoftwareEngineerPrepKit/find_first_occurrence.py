# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/first-occurrence-in-event-code-log/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def findFirstOccurrence(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = findFirstOccurrence(nums, target)

    print(result)
