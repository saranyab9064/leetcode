#============================================================================
# Name        : 24_right_rotate_array.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""
189. Rotate Array
Easy

2084

730

Add to List

Share
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new_list = []
        for i in range(len(nums)-k,len(nums)):
            new_list.append(nums[i])
        for j in range(0,len(nums)-k)  :
            new_list.append(nums[j])
        print(new_list)
        nums = new_list
        print(nums)

        # another approach

        if not nums:
            return nums
        else:
            for i in range(k):
                temp = nums.pop()
                nums.insert(0, temp)

if __name__ == "__main__":
    test = Solution()
    nums = [-1,-100,3,99]
    k = 2
    test.rotate(nums, k)
