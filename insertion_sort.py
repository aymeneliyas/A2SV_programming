#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    """
    23683
    2 4 6 8 8 
    2 4 6 6 8 
    2 4 4 6 8 
    2 3 4 6 8 
    """
    num = arr[n-1]
    ptr = n - 2
    while num < arr[ptr] and ptr >-1:
        arr[ptr+1] = arr[ptr]
        ptr -= 1
        print(*arr,sep=" ")
    
    arr[ptr+1] = num
    print(*arr,sep=" ")
            
         
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

