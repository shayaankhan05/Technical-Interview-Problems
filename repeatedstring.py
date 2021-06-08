#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):

    # My algorithm but it dosent satify all test cases because of memory error
    count_a = 0
    if (n >= 1 and n <= pow(10, 6)) and (len(s) >= 1 and len(s) <= 100):
        s = s * n
        finalString = []
        for i in s[0: n]:
            finalString.append(i)
        for i in finalString:
            if i == 'a':
                count_a += 1
        return count_a
    else:
        return n
    # proper algorithm
    r = 0
    l = len(s)
    for i in range(0, l):
        if s[i] == 'a':
            r += 1
    r *= int(n / l)
    for i in range(0, n % l):
        if s[i] == 'a':
            r += 1
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
