"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return int(num1)*int(num2)
if __name__ == '__main__':
    integer = Solution()
    num1 = "123"
    num2 = "456"
    res = integer.multiply(num1, num2)
    print(res)