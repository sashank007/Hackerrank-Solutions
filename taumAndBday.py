#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    gifts = [b,w]
    giftsCost = [bc,wc]
    if(abs(bc-wc)>z):
        minimumCost = min(giftsCost)
        if(minimumCost==giftsCost[0]):
            return gifts[0]*giftsCost[0] + gifts[1]*(giftsCost[0]+z)
        if(minimumCost==giftsCost[1]):
            return gifts[0]*(giftsCost[1]+z) + gifts[1]*(giftsCost[1])
    else:
        return gifts[0]*giftsCost[0] + gifts[1]*giftsCost[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
