# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 20:17:38 2018

@author: sasha
"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    
    distanceA = abs(z-x)
    distanceB = abs(z-y)
    if(distanceA==distanceB):
        return "Mouse C" 
    if(distanceA<distanceB):
        return "Cat A"
    return "Cat B"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        xyz = raw_input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
