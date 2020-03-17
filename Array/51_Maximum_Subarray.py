

# ============================================================================
# Name        : 51_Maximum_Subarray.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need two nested loops
        # one loop : picks starting element
        # other loop : considers all the elements on right of picked elements as ending element of subarray
        # select the starting point
        """
        list1 = []
        sum = 0
        ans = 0
        for i in range(len(nums)):
            ans = ans + nums[i]
            print(ans)
            if ans > sum:
                sum = ans
            list1.append(nums[i])
            
        # this algorithm will work for positive nos & mix of +ve and -ve's
        if len(nums)==1 and nums[0]< 0: return nums[0]
        n = len(nums)
        ans = 0
        max_sum = 0
        for i in range(0, n):
            max_sum = 0
            for j in range(i, n):
                    max_sum = max_sum + nums[j]
                    if ans < max_sum:
                        ans = max_sum
                    elif max_sum < 0:
                        max_sum = nums[j]
            
        return ans
        """
       # kadane's algorithm is slightly modified to support both -ve and +ve element in an array
       # algorithm description
       # 
       # initialise mesf and meh as first element and zero
        max_element_so_far = nums[0] # -2 initiallu
        max_ending_here = 0
        # iterate each element in an array
        for each_element in range(0,len(nums)): # when i =0 nums[0] = -2
           # meh will be initially first element and later on it will be added up with subarray element
            max_ending_here = max_ending_here + nums[each_element] # meh will be 0+(-2)
            # check if meh is lesser than current element and set meh as current one
            if max_ending_here < nums[each_element]: # -2 < 0
                max_ending_here = nums[each_element] # set as -2
                # check if mesf is lesser than meh 
            if max_element_so_far < max_ending_here: # -2<-2 cond fails
                max_element_so_far = max_ending_here
        return max_element_so_far


if __name__ == '__main__':
    n = [-2,1,-3,4,-1,2,1,-5,4]
    test = Solution()
    ans = test.maxSubArray(n)
    print(ans)

