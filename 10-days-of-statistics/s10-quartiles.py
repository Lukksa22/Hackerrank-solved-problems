#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def get_median(arr):
    half = len(arr)//2
    if len(arr)% 2==0:
        med = arr[half-1:half+1]
        med = sum(med)/len(med)
    else:
        med = arr[half]
    return int(med)

def quartiles(arr):
    arr.sort()
    half = len(arr)/2
    
    qs = [get_median(arr[:math.floor(half)]),
          get_median(arr),
          get_median(arr[math.ceil(half):])
          ]
          
    return qs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
