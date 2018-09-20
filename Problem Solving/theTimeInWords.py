#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
words=[ 
        "o' clock",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"]
minutes=[""]
def timeInWords(h, m):
    if m>30:
        h=h+1
        m=60-m
        if m==15:
            return "quarter to " + words[h]
        return words[m] +  " minutes to " + words[h]
    elif m<=30:
        
        if m==30:
            return "half past " + words[h]
        elif m==0:
            return words[h] + " " + words[m]
        elif m==15:
            return "quarter past " + words[h]
        if m>9:
            return words[m] + " minutes past " + words[h]
        else:
            return words[m] + " minute past " + words[h]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
