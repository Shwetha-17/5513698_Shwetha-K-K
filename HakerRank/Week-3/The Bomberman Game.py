#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])

    def explode(g):
       
        full = [["O"] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if g[i][j] == "O":
                    
                    full[i][j] = "."
                    
                    if i > 0:
                        full[i - 1][j] = "."
                    if i < r - 1:
                        full[i + 1][j] = "."
                    
                    if j > 0:
                        full[i][j - 1] = "."
                    # Right
                    if j < c - 1:
                        full[i][j + 1] = "."
        return ["".join(row) for row in full]

 
    if n == 1:
        return grid


    if n % 2 == 0:
        return ["O" * c for _ in range(r)]

   
    first = explode(grid)
    second = explode(first)

 
    return first if n % 4 == 3 else second

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
