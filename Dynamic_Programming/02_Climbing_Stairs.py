

# ============================================================================
# Name        : 02_Climbing_Stairs.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if the no of steps is 0,1 or 2 return the same
        if n == 0:
            return 1
        elif n == 1 or n == 2:
            return n
        else:
            # follow fibonacci methods
            # Probability of climbing stairs either 1 or 2 : n-1 + n-2
            step1 = 1
            step2 = 2
            out = 0
            for i in range(2, n):
                out = step1 + step2
                step1 = step2
                step2 = out
            return step2


if __name__ == '__main__':
    n = 4
    test = Solution()
    ans = test.climbStairs(n)
    print(ans)

