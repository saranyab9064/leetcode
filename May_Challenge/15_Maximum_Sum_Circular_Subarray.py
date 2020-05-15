
#============================================================================
# Name        : 15_Maximum_Sum_Circular_Subarray.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
#============================================================================
"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""

class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        k = self.kadane_algo(A)
        circular_sum = 0
        for i in range(len(A)):
            circular_sum = circular_sum + A[i]
            # multiply the array with -1
            A[i] = -A[i]
            # again find maximum element
        circular_sum = circular_sum + self.kadane_algo(A)
        if circular_sum > k and circular_sum != 0:
            return circular_sum
        else:
            return k

    def kadane_algo(self, A):
        max_element = A[0]
        ending_element = 0
        for element in range(len(A)):
            ending_element = ending_element + A[element]
            if ending_element < A[element]:
                ending_element = A[element]
            if max_element < ending_element:
                max_element = ending_element
        return max_element


if __name__ == '__main__':
    nums = [5, -3, 5]
    Sum = Solution()
    res = Sum.maxSubarraySumCircular(nums)
    print(res)
