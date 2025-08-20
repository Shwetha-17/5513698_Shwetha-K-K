#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    k=k%26
    res=''
    for i in s:
        if 'A' <= i <= 'Z':
            res=res+ chr((ord(i)-ord('A')+k)%26+ord('A'))
        elif 'a' <= i <= 'z':
            res=res+ chr((ord(i)-ord('a')+k)%26+ord('a'))
        else:
            res=res+i
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
