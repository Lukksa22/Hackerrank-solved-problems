#!/bin/python3

import math
import os
import random
import re
import sys

def weird_not_weird(n):
    if n%2==1:
        print("Weird")
    else:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
        else:
            print("Not Weird")
        

if __name__ == '__main__':
    n = int(input().strip())
    weird_not_weird(n)
    
