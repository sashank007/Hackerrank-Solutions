#!/bin/python3

import math
import os
import random
import re
import collections
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a=0
    if 'a' not in s:
        return 0
    x=collections.Counter(s)['a']
    if n%len(s)!=0:
        a=s[:n%len(s)].count('a')
        return (x) * (n//len(s))+(a)
    return math.floor((n*x)/len(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
