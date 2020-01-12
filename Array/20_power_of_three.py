# ============================================================================
# Name        : 20_power_of_three.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif 1162261467 % n == 0:
          return True
        else:
            return False
if __name__ == '__main__':
    integer = Solution()
    n = 9
    res = integer.isPowerOfThree(n)
    print(res)
