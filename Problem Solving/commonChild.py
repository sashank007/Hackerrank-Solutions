#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the commonChild function below.
#recursive method (alternate)
# def leastCommonSub(s1 , s2, alph , bet):
#     if alph==0 or bet==0 :
#         return 0
#     elif s1[alph-1] == s2[bet-1]:
#         print("inside equal condition")
#         return  1 + leastCommonSub(s1 , s2 , alph-1 ,bet-1)
#     else:
#         return max( leastCommonSub(s1 , s2 , alph,bet-1) , leastCommonSub(s1 , s2 , alph-1 , bet))


def commonChild(s1,s2):
    m = len(s1)
    n=len(s2)
    #need to have m+1 x n+1 matrix to satisfy base condition 
    #for example for abcd and abcd => (a,a) must be 0
    dynamicArray = [[None]*(m+1) for i in range(n+1)]
    #need 2 loops running over both strings to populate our dynamic array from 0,0
    for i in range(m+1):
        for j in range(n+1):
            #base condition
            if i==0 or j==0:
                dynamicArray[i][j] =0
            elif s1[i-1]==s2[j-1]:
                dynamicArray[i][j] = 1 + dynamicArray[i-1][j-1]
            else:
                dynamicArray [i][j] = max( dynamicArray[i-1][j] , dynamicArray[i][j-1])
    return dynamicArray[m][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
