# ============================================================================
# Name        : simpleArraySum.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
import os
import sys

def simpleArraySum(arr):
    arr_count=0
    sum=0

    for i in arr:
        sum+=i;
        arr_count+=1
    print(arr_count)
    return sum,arr_count

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    result1,result2 = simpleArraySum(arr)
    print(result1,result2)


