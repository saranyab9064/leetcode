"""
219. Contains Duplicate II
Easy

1226

1338

Add to List

Share
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # optimised solution
        d = {}
        for i,val in enumerate(nums):
            if val in d:            
                for j in d[val]:
                    if abs(i-j) <= k:
                        return True
                d[val].append(i)
            else:
                d[val] = [i]
        return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    if abs(i-j) == k:
                      flag = True
        
        if not flag:
            return False
        else: return True
                

test = Solution()
arr = [1,2,3,1]
d = 3
out = test.containsNearbyDuplicate(arr,d)
print(out)
