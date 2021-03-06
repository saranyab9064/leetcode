#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    list1 = [0]*len(grades)
    for i,v in enumerate((grades)):
          if v % 5 == 0:
            list1[i] = v
          elif v <38:
            list1[i] = v
          else:
              temp =(v/5)
              q = math.ceil(temp)
              print(q,v)
              diff = q * 5 -v
              if diff <3:
                list1[i] = int(q*5)
              else:
                list1[i] = v

    return list1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
