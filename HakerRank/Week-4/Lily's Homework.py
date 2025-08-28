#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    def count_swaps(a, b):
        index_map = {v:i for i,v in enumerate(a)}
        swaps = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                swaps += 1
                swap_idx = index_map[b[i]]
                index_map[a[i]] = swap_idx
                a[i], a[swap_idx] = a[swap_idx], a[i]
        return swaps
    sorted_arr = sorted(arr)
    return min(count_swaps(arr[:], sorted_arr), count_swaps(arr[:], sorted_arr[::-1]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
