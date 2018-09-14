#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    resultArr=[]
    d={}
    for i in range(len(p)):
        d[p[i]] = i+1
    for i in range(1 , len(p)+1):
        resultArr.append(d[d[i]])
    return resultArr
            
                

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
