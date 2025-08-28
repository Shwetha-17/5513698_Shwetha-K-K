#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    s1 = [0]
    s2 = [0]
    s3 = [0]
    for x in h1: s1.append(s1[-1] + x)
    for x in h2: s2.append(s2[-1] + x)
    for x in h3: s3.append(s3[-1] + x)
    s1.pop(0); s2.pop(0); s3.pop(0)
    s1 = set(s1)
    s2 = set(s2)
    s3 = set(s3)
    common = s1 & s2 & s3
    return max(common) if common else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
