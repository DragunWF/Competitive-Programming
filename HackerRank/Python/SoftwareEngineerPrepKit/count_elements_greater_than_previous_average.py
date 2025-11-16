# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#


def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    count = 0
    previousAverages = [responseTimes[0]]
    for i in range(1, len(responseTimes)):
        currentAverage = average(responseTimes[:i])
        if responseTimes[i] > currentAverage:
            count += 1
    return count


def average(values):
    return sum(values) / len(values)


if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
