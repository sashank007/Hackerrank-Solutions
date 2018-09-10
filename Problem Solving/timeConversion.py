#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
        if s[8] =='P' and (int(s[0])*10 + int(s[1]))==12:
            return "12"+":"+s[3]+s[4]+":"+s[6]+s[7]
        if s[8] == 'P':
            hour = int(s[0])*10+int(s[1])+12
            print(hour)
            if(hour>=24):
                hour = hour%24
            print(hour)
            return str(hour)+":"+s[3]+s[4]+":"+s[6]+s[7]
        if s[8] =='A' and (int(s[0])*10 + int(s[1]))!=12:
                    return s[0]+s[1]+":"+s[3]+s[4]+":" +s[6]+s[7]
        if s[8] =='A' and (int(s[0])*10 + int(s[1]))==12:
                    return "00"+":"+s[3]+s[4]+":"+s[6]+s[7]
            
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
