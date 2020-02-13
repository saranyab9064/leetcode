
# ============================================================================
# Name        : 32_plus_one.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
from array import array
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # if list/array is empty just add 1 to the list and return[1]
        if len(digits) == 0:
            return[1]
        # if last element of the list/array contains 9
        elif digits[-1] == 9:
            print(digits)
            # iterate to the list except the last element
            digits = self.plusOne(digits[:-1])
            # add zero at the end
            digits.extend([0])
        else:
            # when last digit does not contain zero eg 123 just add 1 and return 124
            digits[-1] += 1
        return digits




if  __name__  ==  "__main__" :
    test = Solution()
    a = [1,2,9]
    res = test.plusOne(a)
    print(res)
