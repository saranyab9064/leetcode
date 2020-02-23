

# ============================================================================
# Name        : 27_Add_two_strings.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        total_sum = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry = carry + int(num1[i])
                i = i - 1
                print("i",i)
            if j >= 0:
                carry = carry + int(num2[j])
                j = j - 1
                print("j",j)
            total_sum = total_sum + str(carry % 10)
            carry = (carry // 10)
            print(total_sum,carry,i,j)
        return total_sum[::-1]


if __name__ == "__main__":
    test = Solution()
    num1 = "45"
    num2 = "64"
    res = test.addStrings(num1,num2)
    print(res)
