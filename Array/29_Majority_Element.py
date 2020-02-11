# ============================================================================
# Name        : 29_Majority_Element.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution1(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_count = 0
        index = -1
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[i] == nums [j]:
                    count = count +1
                if count > max_count:
                    max_count = count
                    index = i
        if max_count > length/2:
            return nums[index]
        else:
            return -1

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash table implementation
        h = {}
        # count each element in an array
        # maintain it in hash table {element:count}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        flag = False
        for key in h:
            if h[key] > len(nums) / 2:
                flag = True
                return (key)
                break
        if(Flag == False):
            print("No Majority element")
            return -1


if __name__ == '__main__':
    nums = [3,2,3]
    test = Solution()
    ans = test.majorityElement(nums)
    print(ans)
