#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            if s[i+1] == s[-i-1] and s[i+2] == s[-i-2]:
                return i
            else:
                return len(s) - i - 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
