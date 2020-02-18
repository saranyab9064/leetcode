
# ============================================================================
# Name        : 39_Intersection_of_two_arrays.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect = []
        if len(nums2) < len(nums1):
            for i in nums2:
                if i in nums1:
                    if i not in intersect:
                      intersect.append(i)
        elif len(nums1) == len(nums2):
            for i in nums2:
                if i in nums1:
                    if i not in intersect:
                      intersect.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    if i not in intersect:
                      intersect.append(i)
        return intersect

if __name__ == "__main__":
    test = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res = test.intersection(nums1,nums2)
    print(res)
