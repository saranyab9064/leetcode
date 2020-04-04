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

"""
# another solution
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # to reduce the complexity level we need to perform sorting
        nums.sort()
        # declare output as empty list to append the ans later
        output = []
        # initialise three index i,j and k pointing to
        # i -> first element
        # j -> second element
        # k -> last element
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if not temp:
                    output.append([nums[i],nums[j],nums[k]])
                    while j<len(nums)-1 and nums[j] == nums[j + 1] : 
                        j = j + 1
                    while k > 0 and nums[k] == nums[k - 1]: 
                        k = k - 1
                    j = j + 1
                    k = k - 1
                elif temp < 0:
                    j = j + 1
                else:
                     k = k - 1
        return output            
        
"""
if __name__ == '__main__' :
    nums = [-1, 0, 1, 2, -1, -4]
    Sum = Solution()
    Sum.threeSum(nums)

