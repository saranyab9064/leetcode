#============================================================================
# Name        : 15_find_first_last_position_sorted_array.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0,len(nums)):
            if nums[i] == target:
                start = i
                break

        else:
            return [-1,-1]

        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target:
                end = j
                break
        return [start,end]



if __name__ == "__main__":
    Range = Solution()
    nums = [5,7,7,8,8,10]
    target = 7
    res = Range.searchRange(nums,target)
    print(res)
