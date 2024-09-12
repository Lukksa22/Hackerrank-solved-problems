#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def dayOfProgrammer(year):
    leap_year = False
        
    # our exception
    if year==1918:
        return f"26.09.{year}"
        
    # Julian calendar
    if year<1918:
        if year % 4==0:
            leap_year = True
    else:
        if year % 400==0 or (year % 4==0 and year % 100!=0):
            leap_year = True
        
    if leap_year:
        date = f'12.09.{year}'
    else:
        date = f'13.09.{year}'
        
    return date
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
