# ============================================================================
# Name        : 14_search_insert_position.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
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
              list1 =[]
              list1.append(target)
              list2 = nums + list1
              list3 = sorted(list2)
              for j in range(0,len(list3))  :
                  if list3[j] == target:
                      return j
                      break





if __name__ == '__main__':
    index = Solution()
    nums = [1,3,5,6]
    target = 2
    index_nums = index.searchInsert(nums, target)
    if index_nums != -1:
      print("index",index_nums)
