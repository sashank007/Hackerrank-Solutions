#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    rng = len(s)//3
    count=0
    j = 0
    while ( j<len(s)):
        val1 = s[j]
        val2=s[j+1]
        val3=s[j+2]
        if val1!='S':
            count+=1
        if val2!='O':
            count+=1
        if val3!='S':
            count+=1
        j = j+3
        print(val1 , val2 , val3)
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
