"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # we are going to use xor operation for binary number
        # at the same time we need to keep track of xor operation to stop
        # for that we are performing the orginal binary value to right shift
        # and the same time perform the xor operation by shifting the number to left one by one

        # for right shift we are declaring the variable
        temp = num
        # for xor operation we are declaring the variable
        bit = 1
        while temp:
            print(num)
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        return num 


        """
        # Coverting decimal to binary
        bin_val = ""
        while num > 1: 
          q = num//2         
          bin_val = bin_val+ str(num%2)
          num = q
        # We want to take the complement
        print(bin_val)
        comp_val = ""
        for i in range(len(bin_val)):
            if bin_val[i] == "1":
               comp_val = comp_val+'0'
            else:
                comp_val = comp_val +'1'

        # converting complement binary number to decimal

        binary1 = int(comp_val) 
        decimal, i = 0, 0
        while(binary1 != 0): 
            dec = binary1 % 10
            decimal = decimal + dec * pow(2, i) 
            binary1 = binary1//10
            i += 1
        return decimal

       """


        
if __name__ == "__main__":
    
    in1 = 2
    test = Solution()
    out1 = test.findComplement(in1)
    print(out1)
