#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    worst=scores[0]
    best=scores[0]
    noOfWorst=0
    noOfBest=0
    for i in range(len(scores)):
        if(scores[i]>best):
            noOfBest+=1
            best=scores[i]
        elif(scores[i]<worst):
            noOfWorst+=1
            worst=scores[i]
    return [noOfBest,noOfWorst]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
