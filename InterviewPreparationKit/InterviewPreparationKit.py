#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n  = len(arr)
    dynamicArr = [None]*n
    #base cases as first value is always max and second should be max of second and dp
    dynamicArr[0] = arr[0]
    dynamicArr[1] = max(dynamicArr[0],arr[1])
    #iterate over array to find the max value of alternate subset
    #each time max value till now is stored in dp[i]
    for i in range(2 ,n):
        dynamicArr[i]= max(dynamicArr[i-1] , arr[i] , arr[i]+ dynamicArr[i-2])
    return dynamicArr[-1]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
