# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-number-pairs/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
    count = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] <= budget:
                count += 1
    return count

if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    budget = int(input().strip())

    result = countAffordablePairs(prices, budget)

    print(result)

