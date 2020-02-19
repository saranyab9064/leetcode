

# ============================================================================
# Name        : 40_Contains_Duplicate.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """one solution
        list1 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
            else:
                return True
                break
        return False
        """
        # create a dict
        h ={}
        # set flag value
        flag =  False
        # iterate in from o to len(nums)
        for i in range(len(nums)):
            # store the elements along with count value in the dictionary
            if nums[i] in h:
                h[nums[i]] += 1
            else:
                h[nums[i]] = 1
        # iterate key(i.e h[element] > count(1) in hash table
        # return True
        for key in h:
            if h[key] > 1:
                flag = True
                break
        if flag:
            return True
        else:
            return False





if __name__ == "__main__":
    test = Solution()
    nums1 = [1,2,3,4,1]
    res = test.containsDuplicate(nums1)
    print(res)
