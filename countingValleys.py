

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    valleys = 0
    sealevel = 0
    for step in path:
        if step == 'U':
            sealevel += 1
        else:
            sealevel += -1
        if step == 'U' and sealevel == 0:
            valleys += 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
