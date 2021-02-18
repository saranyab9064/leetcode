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

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        p = 0
        q = 0
        
        res = []
        while p<len(nums1) and q < len(nums2):
            
            if nums1[p] == nums2[q]:
                res.append(nums1[p])
                p += 1
                q += 1
            elif nums1[p] < nums2[q]:
                p += 1
            else:
                q += 1
        
        return res
        
        
        
