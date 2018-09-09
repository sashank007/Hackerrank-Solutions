# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 18:55:40 2018

@author: sasha
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def convertArray(s):
    arr = []
    for i in range(len(s)-1):
            if s[i]=='U':
                arr.append(1)
            else:
                arr.append(-1)
    return arr
            
def countingValleys(n, s):
    start=0
    total=0
    prevStart=0
    s = convertArray(s)
    for i in range(len(s)-1):
        prevStart=start
        start = start+s[i]
        if(start<0):
            if(prevStart==0):
                total+=1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
