#============================================================================
# Name        : 25_fibonacci_number.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.
"""
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        first_element = 0
        second_element = 1
        
        if N == 0:
            return first_element
        elif N == 1:
            return second_element
        else: 
            for x in range(1, N):
                next = first_element + second_element
                first_element = second_element
                second_element = next
            return second_element
            
if __name__ == "__main__":
    test = Solution()
    a = test.fib(3)
    print(a)            
            
