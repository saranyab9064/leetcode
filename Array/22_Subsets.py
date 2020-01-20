# ============================================================================
# Name        : 22_subsets.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        power = pow(2,n)

        i = 0
        j = 0
        list1 = [[]]
        # print all the subsets
        for i in range(0,power):
            for j in range(0,n):
                if((i & (1<<j))> 0):
                    print(nums[j])
            print("")
            
            
from itertools import combinations
class Solution1:
    def subsets(self, S):
       if S == []:
          return []
       res=[[]]
       for element in S:
            temp = []

            for ans in res:
                 #append the new int to each existing list
                temp.append(ans+[element])

            res += temp
       print(res)
       return res
       
       
def powerset(nums):
    result = []
    for size in range(len(nums) + 1):
        result += combinations(nums, size)
    return result
    
    
if __name__ == "__main__" :
        nums = [1,2]
        test = Solution1()
        a = test.subsets(nums)
        print(a)
        """
        test = Solution()
        test.subsets(nums)
        """
