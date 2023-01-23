#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    numofswap = 0
    for row in range(len(a)):
        for col in range(len(a)-1):
            if a[col] > a[col+1]:
                a[col],a[col+1] = a[col+1],a[col]
                numofswap += 1
    print(f"Array is sorted in {numofswap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
                
                
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

