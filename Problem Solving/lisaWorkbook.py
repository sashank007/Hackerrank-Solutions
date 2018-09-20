#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    pages=0
    specialPages=0
    for i in range(len(arr)):
        if(arr[i]<=k):
            pages+=1
            if pages<=arr[i]:
                    specialPages+=1
        elif(arr[i]>k):
            problems=list(range(1,arr[i]+1))
            while(len(problems)!=0):
                pages+=1
                if(pages in problems[:k]):
                    specialPages+=1
                problems=problems[k:]
    return specialPages
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
