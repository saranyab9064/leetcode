


# ============================================================================
# Name        : 42_Ugly_Number.py
# Author      : Saranya Balakrishnan
# Mail Id     : saranyab0925@gmail.com
# ============================================================================
"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # check whether the given num is within range [-2^31 to 2^31-1] 32 bit range
        if num > 0 and num <2147483647:
            # create a list
            list_of_factors = []
            i = 2
            # run loop when given no is greater than 1
            while num > 1:
                # check whether the given number is divided by i and leaves remainder zero
                if num % i == 0:
                    # if remainder is zero then append the value
                    list_of_factors.append(i)
                    # deduce the value of num
                    num = num/ i
                    # deduce the value of i
                    i = i - 1
                    #print(i)
                i += 1
            print(list_of_factors)

            Ugly_list = [2,3,5]
            for j in range(0,len(list_of_factors)):
                print("i",list_of_factors[j])
                if list_of_factors[j] not in Ugly_list:
                     return False
            return True
        else:
            return False
"""
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1
"""








if __name__ == "__main__":
    valid = Solution()
    s = -20
    res = valid.isUgly(s)
    print(res)
