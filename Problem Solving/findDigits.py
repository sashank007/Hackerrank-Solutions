#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    number = str(n)
    number=list(number)
    divisors=0
    for i in range(len(number)):
        if(int(number[i])!=0 and (n%int(number[i]))==0):
            divisors+=1
    return divisors

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
