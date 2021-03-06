#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    rowSum=[]
    for i in range(n):
        s=sum(container[i])
        rowSum.append(s)
    colSum = [ sum(col) for col in zip(*container)]
    colSum.sort()
    rowSum.sort()
    if(colSum==rowSum):
        return 'Possible'
    return 'Impossible'
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
