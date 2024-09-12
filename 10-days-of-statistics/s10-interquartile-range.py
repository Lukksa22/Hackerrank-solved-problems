#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def get_median(arr):
    half = len(arr)//2
    if len(arr)% 2==0:
        med = (arr[half-1] + arr[half]) /2
    else:
        med = arr[half]
    return med

def quartiles(arr):
    arr.sort()
    half = len(arr)/2
    
    qs = [get_median(arr[:math.floor(half)]),
          get_median(arr),
          get_median(arr[math.ceil(half):])
          ]
          
    return qs

def interQuartile(values, freqs):
    arr = [values[j] for j in range(len(freqs)) for i in range(freqs[j])]
    arr.sort()
    qs = quartiles(arr)
    print(f"{qs[2] - qs[0]:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
