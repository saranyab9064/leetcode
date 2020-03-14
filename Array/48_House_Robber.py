
# ============================================================================
# Name        : 48_House_Robber.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        n = len(nums)
        sum1 = 0
        sum2 = 0
        for i in range(0,n,2):
            sum1 = sum1 + nums[i]
        for j in range(1,n,2):
            sum2 = sum2 + nums[j]
        return(max(sum1,sum2))
        """
        # initialise val2 & val1
        val2 = 0
        val1 = 0
        for i in range(0,len(nums)):
            # set temp and val2 value
            # add val2 with current value and find max between val1 and added value
            temp = val1
            val1 = max(val2+nums[i],val1)
            val2 = temp
        return val1





if __name__ == '__main__':
    n = [2,7,9,3,1]
    test = Solution()
    out = test.rob(n)
    print(out)
