
# ============================================================================
# Name        : 55_Two_Sum_II.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_index = 0
        r_index = len(numbers) - 1

        while l_index < r_index:
            sum_of_two_nos = numbers[l_index] + numbers[r_index]
            if sum_of_two_nos < target:
                l_index = l_index + 1
            elif sum_of_two_nos > target:
                r_index = r_index - 1
            else:
                return l_index + 1, r_index + 1
        return -1, -1



if __name__ == '__main__':
    test=Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    out = test.twoSum(numbers,target)
    print(out)
