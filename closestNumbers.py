#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    minimum = sys.maxsize
    arr.sort()
    result=[]
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])<minimum:
            minimum=abs(arr[i] - arr[i+1])
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])==minimum:
            result.append(arr[i])
            result.append(arr[i+1])
    print(minimum)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
