#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    d={}
    alphas = list('abcdefghijklmnopqrstuvwxyz')
    heightsArray=[]
    for i in range(0,26):
        d[alphas[i]] = h[i]
    word=list(word)
    for i in range(len(word)):
        heightsArray.append(d[word[i]])
    return max(heightsArray)*len(heightsArray)
  
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
