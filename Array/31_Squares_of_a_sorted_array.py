
# ============================================================================
# Name        : 31_Squares_of_a_sorted_array.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in A:
            new_list.append(i*i)
        return (sorted(new_list))
if __name__ == '__main__':
    nums1 = [-7,-3,2,3,11]
    test = Solution()
    ans = test.sortedSquares(nums1)
    print(ans)
