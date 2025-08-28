#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < q:
        if is_prime(num):
            primes.append(num)
        num += 1

    result = []
    for i in range(q):
        A = []
        B = []
        prime = primes[i]
        while number:
            plate = number.pop()
            if plate % prime == 0:
                B.append(plate)
            else:
                A.append(plate)
        result.extend(B[::-1])
        number = A
    result.extend(number[::-1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
