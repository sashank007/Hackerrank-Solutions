#!/bin/python3

import math
import os
import random
import re
import sys
import logging

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    resultArr=[]
    for i in range( p ,q+1):
        d=len(str(i))
        squared  = i*i
        squared=str(squared)
        while(len(squared)!=2*d):
            squared='0'+squared
        a=squared[:d]
        b=squared[d:]
        summing = int(a)+int(b)
        if(summing==i):
            resultArr.append(i)
    if len(resultArr)!=0:
        for i in range(len(resultArr)):
            print(str(resultArr[i]) , end = ' ')
    else:
        print("INVALID RANGE")
            
        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
