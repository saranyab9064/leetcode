#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    jump = 0
    index = 0
    while index < n-1:
        if index+2<n and c[index+2]==0:
            jump = jump+1
            index = index+2
        elif index + 1<n and c[index+1]==0:
            jump = jump + 1
            index = index+1

    return jump
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
