#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    distances=[]
    for i in range(len(a)):
        if a[i] in  a[i+1:]:
            distances.append(a[i+1:].index(a[i]) + 1 )
            print(distances)
    if len(distances)==0:
        return -1
    return min(distances)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
