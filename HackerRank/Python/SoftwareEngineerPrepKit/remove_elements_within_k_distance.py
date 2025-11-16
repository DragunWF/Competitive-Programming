# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/remove-elements-within-k-distance/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    i = 1
    while i < len(timestamps):
        prev = timestamps[i - 1]
        cur = timestamps[i]
        if cur - prev < K:
            timestamps.pop(i)
            i = 1
        else:
            i += 1
    return len(timestamps)

if __name__ == '__main__':
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)

    K = int(input().strip())

    result = debounceTimestamps(timestamps, K)

    print(result)
