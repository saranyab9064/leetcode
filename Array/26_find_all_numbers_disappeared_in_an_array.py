# ============================================================================
# Name        : 26_find_all_numbers_disappeared_in_an_array.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # wrong one
        nums = sorted(nums)
        new_list = []
        for i in nums:
            if i not in new_list:
                new_list.append(i)
        list1 =[]
        for j in range(0,len(new_list)-1):
            if new_list[j]+1 != new_list[j+1]:
                new_list.append(new_list[j]+1)
        new_list = sorted(new_list)
        for k in range(0,len(new_list)-1):
            if new_list[k]+1 != new_list[k+1]:
                new_list.append(new_list[k]+1)
        for i in new_list:
            if i not in nums:
                list1.append(i)
        return(sorted(list1))

       # correct one
    class Solution(object):
        def findDisappearedNumbers(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            new_list = []
            for i in range(1, len(nums) + 1):
                new_list.append(i)
            a = set(new_list)
            b = set(nums)
            return list(a - b)


if __name__ == "__main__":
    test = Solution()
    nums = [4,3,2,7,8,2,3,1,10]
    ans = test.findDisappearedNumbers(nums)
    print(ans)
