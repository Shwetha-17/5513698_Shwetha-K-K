#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

MOD = 1000000007

def legoBlocks(n, m):
    ways = [0] * (m + 1)
    ways[0] = 1
    for i in range(1, m + 1):
        ways[i] = (ways[i - 1] + (ways[i - 2] if i >= 2 else 0) + (ways[i - 3] if i >= 3 else 0) + (ways[i - 4] if i >= 4 else 0)) % MOD
    total = [pow(ways[i], n, MOD) for i in range(m + 1)]
    solid = [0] * (m + 1)
    solid[0] = 1
    for i in range(1, m + 1):
        s = total[i]
        for j in range(1, i):
            s -= solid[j] * total[i - j]
        solid[i] = s % MOD
    return solid[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
