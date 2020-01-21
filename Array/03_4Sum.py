#============================================================================
# Name        : 03_4Sum.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#============================================================================
"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(i + 2, len(nums)):
                    for l in range (i + 3, len(nums)):
                        a = nums[i];
                        b = nums[j];
                        c = nums[k];
                        d = nums[l];
                        if a + b + c + d == target:
                            temp += [[a,b,c,d]]
                            flag = True
        if flag == False:
            return -1
        else:
            return temp

if __name__ == '__main__' :
    nums = [1, 0, -1, 0, -2, 2]
    nums = sorted(nums)
    print(nums)
    target = 0
    Sum = Solution()
    res = Sum.fourSum(nums,target)
