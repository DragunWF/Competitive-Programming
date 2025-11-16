# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-smallest-missing-positive-integer/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    smallestMissingPositiveNum = 1
    while smallestMissingPositiveNum in orderNumbers:
        smallestMissingPositiveNum += 1
    return smallestMissingPositiveNum


if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
