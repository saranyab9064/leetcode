# ============================================================================
# Name        : 28_move_zeroes.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0  # Count of non-zero elements
  
        for i in range(len(nums)):
            if nums[i]:
                nums[count] = nums[i]
                count += 1
        for i in range(count,len(nums)):
            nums[i] = 0

        print(nums)



if __name__ == '__main__':
    nums = [0,0,1]
    test = Solution()
    test.moveZeroes(nums)

