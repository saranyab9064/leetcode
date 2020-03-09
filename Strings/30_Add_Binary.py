
# ============================================================================
# Name        : 30_Add_binary.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ==========================================================================
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """



        # if length of a or b is zero return the otherone
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        # find the maximum length
        maximum_len = max(len(a),len(b))
        # append zero based on maximum length using zfill method() eg 11 become 0011
        a = a.zfill(maximum_len)
        b = b.zfill(maximum_len)
        # initialize the sum as empty list and carry as zero
        sum = []
        carry = 0
        # traverse the string from the last digit
        for i in range(maximum_len-1,-1,-1):
            # check if the last digit of a is 1
             if a[i] == '1':
                 # if last digit of a is 1 and incr the carry by 1
                 carry += 1
             if b[i] == '1':
                 carry += 1
             print(carry)
                # if carry if divisible by 2 which leaves remainder zero then append 0 to the sum else 1
             if carry % 2 == 1:
                sum.append('1')
             else:
                 sum.append('0')
             # store the quotient
             carry //= 2
        # after iteration if carry is 1 in the last append 1 else 0 and reverse the sum
        if carry == 1:
            sum.append('1')
        print(sum)
        sum.reverse()
        print(sum)

        return ''.join(sum)




if __name__ == "__main__":
    test = Solution()
    a = '11'
    b = '01'
    res = test.addBinary(a,b)
    print(res)

