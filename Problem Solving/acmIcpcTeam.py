#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the acmTeam function below.
def acmTeam(topic):
    count=0
    resultArray=[]
    maxSubjects= 0
    for v ,w in itertools.combinations( range ( len(topic)) , 2):
            sumPair  = bin(int(topic[v] , 2) |int( topic[w] , 2))
            if(sumPair.count('1')==maxSubjects):
                    count+=1
            elif(sumPair.count('1') > maxSubjects):
                     maxSubjects = sumPair.count('1')
                     count=1
    resultArray.append(maxSubjects)
    resultArray.append(count)
    return resultArray
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
