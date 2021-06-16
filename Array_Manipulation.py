#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

#  for some test cases time complexity exceeds for my algorithm


def arrayManipulation(n, queries):
    A = [0] * (n + 1)
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]

        for l in range(a, b+1):
            A[l] = A[l] + k

    return(max(A))

#  better approach


def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    max_value = 0
    total_sum = 0

    for query in queries:
        l = query[0]
        h = query[1]
        val = query[2]
        arr[l-1] = arr[l-1] + val
        arr[h] = arr[h]-val
    for value in arr:
        total_sum = total_sum + value
        max_value = max(max_value, total_sum)
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
