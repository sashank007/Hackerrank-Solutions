#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def findOdds(arr):
    odds=0
    for i in arr:
        if i%2!=0:
            odds+=1
    return odds
def gameOfThrones(s):
    d=[0]*26
    for i in s:
        d[ord(i)-ord('a')]+=1
    if findOdds(d)>1:
        return "NO"
    else:
        return "YES"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
