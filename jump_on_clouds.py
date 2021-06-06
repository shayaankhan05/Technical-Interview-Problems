#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    i = 0
    n = len(c) - 2
    jump = 0
    for i in range(n):
        if (c[i] == 0 and (c[i+1] == 0 and c[i+2] == 0)):
            jump += 1
            i += 1
        elif (c[i] == 0 and (c[i+1] == 1 and c[i+2] == 0)):
            jump += 1
            i += 1
        elif (c[i] == 0 and c[i+1] == 0):
            jump += 1
        elif (c[i] == 1):
            continue
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
