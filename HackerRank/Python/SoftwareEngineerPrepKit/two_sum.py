# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/time-slot-task-pairing/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#

def findTaskPairForSlot(taskDurations, slotLength):
    seen = {}
    for i, duration in enumerate(taskDurations):
        complement = slotLength - duration
        if complement in seen:
            return [seen[complement], i]
        seen[duration] = i
    return [-1, -1]

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
