#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    dictionary = {}
    setOfArr = set(arr)
    maxId = 0
    maxCount = 0
    for val in setOfArr:
        count = arr.count(val)
        dictionary[val]=count
    print("dictionary -->"  , dictionary)
    for key,val in dictionary.items():
        if(val==maxCount):
            if(key<maxId):
                maxId=key
        if(val>maxCount):
            print("key , value -->" , key,val)
            maxCount=val
            print("max count " ,maxCount)
            maxId =key
    return maxId
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
