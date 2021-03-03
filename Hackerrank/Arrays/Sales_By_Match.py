#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {}
    res = 0
    for i in range(n):
        if ar[i] not in d:
            d[ar[i]] = 1
        else:
            d[ar[i]] += 1
        
    for key,value in d.items():
        res = res + value//2
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
