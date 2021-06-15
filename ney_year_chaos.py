#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    n = len(q)
    bribes = 0
    for I in range(1, n+1):
        index = q.index(I)

        if I - index > 3:
            bribes = "Too chaotic"
            break
        for j in range(index):
            if q[j] > I:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
