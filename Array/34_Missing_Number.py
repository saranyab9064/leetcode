
# ============================================================================
# Name        : 34_Missing_Number.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================


"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        length = len(nums)
        nums = sorted(nums)
        for i in range(length-1):
            if nums[i]+1 != nums[i+1]:
                return nums[i]+1
        return -1
        """
        n = len(nums)
        # sum of numbers from 0 to n
        total = n*(n+1)/2
        sum_of_nums = sum(nums)
        return total - sum_of_nums
"""
    length = len(nums) + 1
    nums = sorted(nums)
    # convert to set
    temp = set(nums)
    for i in range(length):
    # iterate the i from 0 to length  
    # if i not in the set return i
        if i not in temp:
            return i
"""            

if __name__ == "__main__":
    test = Solution()
    a = [9,6,4,2,3,5,7,0,1,8]
    res = test.missingNumber(a)
    print(res)
