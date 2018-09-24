#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    x=n*k
    x=int(x)%9
    print( x if x else 9)

n, k = map(int, input().split())
superDigit(n,k)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nk = input().split()

#     n = nk[0]

#     k = int(nk[1])

#     result = superDigit(n, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()
