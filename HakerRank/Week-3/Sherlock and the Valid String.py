#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    
    freq = Counter(s)
    freq_values = list(freq.values())

  
    freq_count = Counter(freq_values)

    
    if len(freq_count) == 1:
        
        return "YES"
    
    if len(freq_count) > 2:
       
        return "NO"
    
  
    min_freq = min(freq_count.keys())
    max_freq = max(freq_count.keys())

   
    if freq_count[min_freq] == 1 and min_freq == 1:
        return "YES"
    

    if freq_count[max_freq] == 1 and max_freq - min_freq == 1:
        return "YES"


    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
