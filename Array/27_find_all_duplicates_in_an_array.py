# ============================================================================
# Name        : 27_find_all_duplicates_in_an_array.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        new_list = []
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                new_list.append(nums[i])
        return(sorted(new_list))


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    test = Solution()
    ans = test.findDuplicates(nums)
    print(ans)
