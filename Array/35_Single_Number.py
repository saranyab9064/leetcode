
# ============================================================================
# Name        : 35_Single_Number.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================


"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash table implementation; initiate h as empty dict
        h = {}
        # set bool value for flag variable
        flag = False
        # count each element in an array
        # maintain it in hash table {element:count}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        # iterate key(i.e h[element] = count(1) in hash table
        # return element
        for key in h:
            if h[key] == 1:
                flag = True
                return (key)
                break
        # else return no element in an array which has count 1
        if (Flag == False):
            return -1
if __name__ == "__main__":
    test = Solution()
    a = [2,2,1]
    res = test.singleNumber(a)
    print(res)
