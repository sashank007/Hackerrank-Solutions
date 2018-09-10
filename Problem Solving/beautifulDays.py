#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days=0
    for x in range( i , j+1):
        numb = x 
        revNumb  = 0  
        Number  = numb
        while(Number > 0):    
            Reminder = Number %10    
            revNumb = (revNumb *10) + Reminder    
            Number = Number //10 
        print(revNumb   , numb)
        if(abs(revNumb - numb)%k==0):
            days+=1
    return days
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
