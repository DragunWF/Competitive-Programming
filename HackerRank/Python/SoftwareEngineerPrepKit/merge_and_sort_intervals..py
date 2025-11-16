# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/merge-and-sort-intervals/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda item: item[0])
    merged_list = intervals[0]
    output = []
    for i in range(1, len(intervals)):
        if merged_list[1] >= intervals[i][0]:
            merged_list[1] = max(intervals[i][1], merged_list[1])
        else:
            output.append(merged_list)
            merged_list = intervals[i]
    output.append(merged_list)
    return output

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
