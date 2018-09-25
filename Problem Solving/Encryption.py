#!/bin/python

import math

import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    length = len(s)
    s=list(s)
    s2=[None]*length
    for i in range(len(s2)):
        s2[i]=s.pop()
        print(s2[i])
    rows = int(math.floor(math.sqrt(length)))
    cols = int(math.ceil(math.sqrt(length)))
    if ( rows*cols)<length:
        rows+=1
    print(rows,cols)
    result = [[None]*(cols) for i in range(rows)]
    resultstr=""
    for i in range(rows):
        for j in range(cols):
            if len(s2)!=0:
                result[i][j]=s2.pop()
                print(s2)
    print(result)
    for i in range(cols):
        for j in range(rows):
            if result[j][i]!=None:
                resultstr+=result[j][i]
            if j==rows-1:
                resultstr+=" "
    print(result)
    return resultstr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
