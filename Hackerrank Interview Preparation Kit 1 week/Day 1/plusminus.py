#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    total = len(arr)
    
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
        
    pr = positive_count/total
    nr = negative_count/total
    zr = zero_count/total
    
    print(f"{pr:.6f}")
    print(f"{nr:.6f}")
    print(f"{zr:.6f}")
            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
