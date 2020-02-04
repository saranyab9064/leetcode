#============================================================================
# Name        : 25_Sqrt(x).py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # return int(math.sqrt(x))
        if x==0 or x==1:
            return x
        else:
            start = 0
            end = x
            while (start <= end):
                mid_val = int((start + end) / 2)
                if (mid_val * mid_val == x):
                    return mid_val
                elif (mid_val * mid_val < x):
                    start = mid_val + 1
                    val = mid_val
                else:
                    end = mid_val - 1
            return val

if __name__ == "__main__":
    test = Solution()
    ans = test.mySqrt(16)
    print(ans)
