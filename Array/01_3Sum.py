#============================================================================
# Name        : 01_3Sum.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#============================================================================
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(i+2, len(nums)):
                        a = nums[i];
                        b = nums[j];
                        c = nums[k];
                        if a+b+c == 0:
                            print([a, b, c])
                            flag =True
        if flag == False:
            print("sum does not exist")


if __name__ == '__main__' :
    nums = [-1, 0, 1, 2, -1, -4]
    Sum = Solution()
    Sum.threeSum(nums)

