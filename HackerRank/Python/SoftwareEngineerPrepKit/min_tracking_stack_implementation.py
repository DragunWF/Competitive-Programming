# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/min-tracking-stack/problem

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    stack = []
    results = []
    for operation in operations:
        tokens = operation.split(" ")
        command = tokens[0]
        if command == "push":
            num = int(tokens[1])
            stack.append(num)
        elif command == "getMin":
            results.append(min(stack))
        elif command == "pop":
            stack.pop()
        elif command == "top":
            results.append(stack[-1])
    return results

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
