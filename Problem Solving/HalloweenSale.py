#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
        dollars=s
        deduction=d
        minimum=m
        costOfToy=p
        totalToys=0
        if(p<=s):
            totalToys+=1
            dollars=dollars-p
            p=p-m
        else:
            return 0
        while(dollars>=costOfToy):
            if(costOfToy-deduction>minimum):
                costOfToy=costOfToy-deduction
                dollars=dollars-costOfToy
                totalToys+=1
            elif(costOfToy-deduction<=minimum):
                costOfToy=minimum
                dollars=dollars-costOfToy
                totalToys+=1
            print("The cost of toy and dollars left-->" , costOfToy ,dollars)
        return totalToys
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
