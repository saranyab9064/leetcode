#============================================================================
# Name        : 13_search_in_rotated_sorted_array.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#===========================================================================
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
                break
        else:
            return -1


if __name__ == '__main__':
    index = Solution()
    nums = nums = [4,5,6,7,0,1,2]
    target = 11
    index_nums = index.search(nums, target)
    if index_nums != -1:
      print("index",index_nums)
    else :
        print("index not found",index_nums)